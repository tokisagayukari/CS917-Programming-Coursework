import csv
import time
import calendar

"""
    Part C
    Please provide definitions for the following functions
"""


# moving_avg_short(data, start_date, end_date) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_avg_short(data, start_date, end_date):
    # initialize
    moving_avg_short_dict = dict()
    avg_short_list = []
    date_list = []
    # convert from time to epoch timestamp
    start_epoch = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    start_epoch_before = start_epoch - 2 * 86400

    # moving_avg_short for the first two days in the csv.file
    avg_price_1 = float(data[0]['volumeto']) / float(data[0]['volumefrom'])
    date_epoch_1 = int(data[0]['time'])
    dt_1 = time.gmtime(date_epoch_1)
    date_1 = time.strftime("%d/%m/%Y", dt_1)
    avg_price_2 = (avg_price_1 + float(data[1]['volumeto']) / float(data[1]['volumefrom'])) / 2
    date_epoch_2 = int(data[1]['time'])
    dt_2 = time.gmtime(date_epoch_2)
    date_2 = time.strftime("%d/%m/%Y", dt_2)

    if start_epoch == int(data[0]['time']):
        moving_avg_short_dict[date_1] = avg_price_1
        moving_avg_short_dict[date_2] = avg_price_2
        start_epoch += 2 * 86400

    if start_epoch == int(data[1]['time']):
        moving_avg_short_dict[date_2] = avg_price_2
        start_epoch += 86400

    # Start date is after the second row of the csv.file
    # regular condition
    price_each_list = []
    if start_epoch >= int(data[2]['time']):
        for i in range(len(data)):
            row = data[i]
            if start_epoch_before <= int(row['time']) <= end_epoch:
                # price of each day in the period
                price_each = float(row['volumeto']) / float(row['volumefrom'])
                price_each_list.append(price_each)

        for j in range(len(price_each_list)):
            avg_short = sum(price_each_list[j: j + 3]) / 3
            avg_short_list.append(avg_short)
            date_epoch = start_epoch + j * 86400
            dt = time.gmtime(date_epoch)
            date_string = time.strftime("%d/%m/%Y", dt)
            date_list.append(date_string)

        for k in range(len(price_each_list) - 2):
            moving_avg_short_dict[date_list[k]] = avg_short_list[k]

    return moving_avg_short_dict


# moving_avg_long(data, start_date, end_date) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_avg_long(data, start_date, end_date):
    # initialize
    moving_avg_long_dict = dict()
    avg_long_list = []
    date_list = []

    # convert from time to epoch timestamp
    start_epoch = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    start_epoch_before = start_epoch - 9 * 86400

    # moving_avg_short for the first nine days in the csv.file
    special_avg_list = []
    special_date_list = []
    special_price_list = []
    for i in range(len(data)):
        row = data[i]
        if i < 9:
            price_each = float(row['volumeto']) / float(row['volumefrom'])
            special_price_list.append(price_each)

    for j in range(0, 9, 1):
        special_avg = sum(special_price_list[0:j + 1]) / (j + 1)
        special_avg_list.append(special_avg)
        special_date_epoch = int(data[j]['time'])
        dt = time.gmtime(special_date_epoch)
        special_date = time.strftime("%d/%m/%Y", dt)
        special_date_list.append(special_date)

    if start_epoch == int(data[0]['time']):
        moving_avg_long_dict[special_date_list[0]] = special_avg_list[0]
        start_epoch += 86400

    if start_epoch == int(data[1]['time']):
        moving_avg_long_dict[special_date_list[1]] = special_avg_list[1]
        start_epoch += 86400

    if start_epoch == int(data[2]['time']):
        moving_avg_long_dict[special_date_list[2]] = special_avg_list[2]
        start_epoch += 86400

    if start_epoch == int(data[3]['time']):
        moving_avg_long_dict[special_date_list[3]] = special_avg_list[3]
        start_epoch += 86400

    if start_epoch == int(data[4]['time']):
        moving_avg_long_dict[special_date_list[4]] = special_avg_list[4]
        start_epoch += 86400

    if start_epoch == int(data[5]['time']):
        moving_avg_long_dict[special_date_list[5]] = special_avg_list[5]
        start_epoch += 86400

    if start_epoch == int(data[6]['time']):
        moving_avg_long_dict[special_date_list[6]] = special_avg_list[6]
        start_epoch += 86400

    if start_epoch == int(data[7]['time']):
        moving_avg_long_dict[special_date_list[7]] = special_avg_list[7]
        start_epoch += 86400

    if start_epoch == int(data[8]['time']):
        moving_avg_long_dict[special_date_list[8]] = special_avg_list[8]
        start_epoch += 86400

    # regular condition
    price_each_list = []
    if start_epoch >= int(data[9]['time']):
        for k in range(len(data)):
            row = data[k]
            if start_epoch_before <= int(row['time']) <= end_epoch:
                # price of each day in the period
                price_each = float(row['volumeto']) / float(row['volumefrom'])
                price_each_list.append(price_each)

    for m in range(len(price_each_list)):
        avg_long = sum(price_each_list[m: m + 10]) / 10
        avg_long_list.append(avg_long)
        date_epoch = start_epoch + m * 86400
        dt = time.gmtime(date_epoch)
        date_string = time.strftime("%d/%m/%Y", dt)
        date_list.append(date_string)

    for n in range(len(price_each_list) - 9):
        moving_avg_long_dict[date_list[n]] = avg_long_list[n]

    return moving_avg_long_dict


# find_buy_list(short_avg_dict, long_avg_dict) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def find_buy_list(short_avg_dict, long_avg_dict):
    # replace None with an appropriate return value
    buy_list_dict = dict()
    price_comp_dict = dict()
    # Since using python3.7, the dictionaries has been ordered by date according to my add method
    # calculate the D-value of short_avg and long_avg
    for key1, key2 in zip(short_avg_dict.keys(), long_avg_dict.keys()):
        if key1 == key2:
            comp = short_avg_dict[key1] - long_avg_dict[key2]
            price_comp_dict[key1] = comp

    loop_time = range(len(price_comp_dict)-1)
    for i in loop_time:
        day_status = price_comp_dict.popitem()
        if day_status[1] <= 0:
            buy_list_dict[day_status[0]] = 0
        if day_status[1] > 0:
            last_date = list(price_comp_dict.keys())[-1]
            before_status = price_comp_dict.get(last_date)
            if before_status <= 0:
                buy_list_dict[day_status[0]] = 1
            else:
                buy_list_dict[day_status[0]] = 0
    # The first day is always 0
    first_date = list(short_avg_dict.keys())[0]
    buy_list_dict[first_date] = 0
    return buy_list_dict


# find_sell_list(short_avg_dict, long_avg_dict) -> dict
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def find_sell_list(short_avg_dict, long_avg_dict):
    # replace None with an appropriate return value
    sell_list_dict = dict()
    price_comp_dict = dict()
    # Since using python3.7, the dictionaries has been ordered by date according to my add method
    # calculate the D-value of short_avg and long_avg
    for key1, key2 in zip(short_avg_dict.keys(), long_avg_dict.keys()):
        if key1 == key2:
            comp = short_avg_dict[key1] - long_avg_dict[key2]
            price_comp_dict[key1] = comp

    loop_time = range(len(price_comp_dict) - 1)
    for i in loop_time:
        day_status = price_comp_dict.popitem()
        if day_status[1] >= 0:
            sell_list_dict[day_status[0]] = 0
        if day_status[1] < 0:
            last_date = list(price_comp_dict.keys())[-1]
            before_status = price_comp_dict.get(last_date)
            if before_status >= 0:
                sell_list_dict[day_status[0]] = 1
            else:
                sell_list_dict[day_status[0]] = 0
    # The first day is always 0
    first_date = list(short_avg_dict.keys())[0]
    sell_list_dict[first_date] = 0
    return sell_list_dict


# crossover_method(data, start_date, end_date) -> [buy_list, sell_list]
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def crossover_method(data, start_date, end_date):
    buy_list = []
    sell_list = []
    buy_dict = find_buy_list(moving_avg_short(data, Start_Date, End_Date), moving_avg_long(data, Start_Date, End_Date))
    sell_dict = find_sell_list(moving_avg_short(data, Start_Date, End_Date), moving_avg_long(data, Start_Date, End_Date))
    for key1 in buy_dict:
        if buy_dict[key1] == 1:
            buy_list.insert(0, key1)
    for key2 in sell_dict:
        if sell_dict[key2] == 1:
            sell_list.insert(0, key2)
    return [buy_list, sell_list]


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program

    # Example variable initialization
    # data is always the cryptocompare_btc.csv read in using a DictReader

    data = []
    with open("cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]

    # test
    Start_Date = "03/11/2019"
    End_Date = "14/11/2019"
    print(crossover_method(data, Start_Date, End_Date))
    pass
