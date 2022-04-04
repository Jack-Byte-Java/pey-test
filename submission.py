import matplotlib.pyplot as plt
from datetime import datetime

def plot_graph(filename: str):
    file = open(filename, "r", encoding="utf8") #Used to open and read the given file

    parsed = [] #where the parsed data is stored
    line = 1 #read thes each line of the file, initialized to 1 so while loop can start
    months = {'01':'Jan',
            '02':'Feb',
            '03':'Mar',
            '04':'Apr',
            '05':'May',
            '06':'Jun',
            '07':'Jul',
            '08':'Aug',
            '09':'Sep',
            '10':'Oct',
            '11':'Nov',
            '12':'Dec'} #dictionary to translate the months from number to its short formed name

    while line != "":
        info = {}
        for i in range(10):
            line = file.readline()
            data = line.split(";") #replace with ;
            for j in data:
                j = j.strip() #removes any whitespace
                if j.startswith("DIs") and j[3:].isnumeric(): #checks the prefixes
                    info["Issuance Date"] = j[-2:] + "-" + months[j[-4:-2]] + "-" + j[-6: -4]
                if j.startswith("BPr"):
                    info["Clean Bid"] = j[3:]
                if j.startswith("APl"):
                    info["Clean Ask"] = j[3:]
                if j.startswith("Pl"):
                    info["Last Price"] = j[2:]
        if len(info) > 0: #only adds the data if there were any of the require prefixes
            parsed.append(info)

    last_price = {}
    clean_ask = {}
    clean_bid = {}
    for data in parsed: #gives priority to Last Price, then Clean Ask, then Clean Bid to show on the graph
        if "Issuance Date" in data and "Last Price" in data:
            last_price[data["Issuance Date"]] = data["Last Price"]
        elif "Issuance Date" in data and "Clean Ask" in data:
            clean_ask[data["Issuance Date"]] = data["Clean Ask"]
        elif "Issuance Date" in data and "Clean Bid" in data:
            clean_bid[data["Issuance Date"]] = data["Clean Bid"]

    plot_lst_x = []
    plot_lst_y = []
    plot_lst_x_sorted = []
    plot_lst_y_sorted = []

    for k, v in last_price.items(): #adds Last Price and the corresponding Issuance Date
        plot_lst_x.append(k)
        plot_lst_y.append(float(v))

    plot_lst_x_sorted = plot_lst_x.copy()

    plot_lst_x_sorted.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))


    for i in range(len(plot_lst_x_sorted)):
        plot_lst_y_sorted.append(plot_lst_y[plot_lst_x.index(plot_lst_x_sorted[i])])

    plt.scatter(plot_lst_x_sorted, plot_lst_y_sorted, label="Last Price")

    plot_lst_y.clear()
    plot_lst_x.clear()
    plot_lst_y_sorted.clear()
    plot_lst_x_sorted.clear()

    for k, v in clean_ask.items(): #adds Clean Ask and the corresponding Issuance Date
        plot_lst_x.append(k)
        plot_lst_y.append(float(v))

    plot_lst_x_sorted = plot_lst_x.copy()

    plot_lst_x_sorted.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))

    for i in range(len(plot_lst_x_sorted)):
        plot_lst_y_sorted.append(plot_lst_y[plot_lst_x.index(plot_lst_x_sorted[i])])

    plt.scatter(plot_lst_x_sorted, plot_lst_y_sorted, label="Clean Ask")

    plot_lst_y.clear()
    plot_lst_x.clear()
    plot_lst_y_sorted.clear()
    plot_lst_x_sorted.clear()


    for k, v in clean_bid.items(): #adds Clean Bid and the corresponding Issuance Date
        plot_lst_x.append(k)
        plot_lst_y.append(float(v))

    plot_lst_x_sorted = plot_lst_x.copy()

    plot_lst_x_sorted.sort(key=lambda date: datetime.strptime(date, "%d-%b-%y"))

    for i in range(len(plot_lst_x_sorted)):
        plot_lst_y_sorted.append(plot_lst_y[plot_lst_x.index(plot_lst_x_sorted[i])])

    plt.scatter(plot_lst_x_sorted, plot_lst_y_sorted, label="Clean Bid")

    plt.legend()

    plt.xticks(rotation = 45)

    plt.show()


if __name__ == "__main__":
    filename = input("Please type in the file name: ")

    plot_graph(filename)