import csv
import sys
import time
import calendar

"""
    Part B
    Please provide definitions for the following functions *WITH EXCEPTION HANDLERS*
"""


class MyException(Exception):

    # Exception message set by value
    def __init__(self, value):
        self.parameter = value

    # Exception message to be printed
    def __str__(self):
        return self.parameter


# highest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def highest_price(data, start_date, end_date):
    price_list = []

    File_Start_epoch = 1430179200
    File_End_epoch = 1602979200

    # convert from time to epoch timestamp
    try:
        start_epoch = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    except ValueError:
        print("Error: invalid date value")
        sys.exit()

    # custom exception to catch those start larger than end
    try:
        # check error condition
        if end_epoch < start_epoch:
            raise MyException("Error: end date must be larger than start date")
    except MyException as e:
        print(str(e))
        sys.exit()

    # custom exception to catch those outbound the date
    try:
        # check error condition
        if end_epoch > File_End_epoch or start_epoch > File_End_epoch \
                or end_epoch < File_Start_epoch or start_epoch < File_Start_epoch:
            raise MyException("Error: date value is out of range")
    except MyException as e:
        print(str(e))
        sys.exit()

    # find those satisfying the periods
    try:
        for i in range(len(data)):
            row = data[i]
            if start_epoch <= int(row['time']) <= end_epoch:
                price_list.append(row['high'])
    except KeyError:
        print("Error: requested column is missing from dataset")
        sys.exit()

    # find the highest value and return the value
    max_price = float(price_list[0])
    for j in range(len(price_list)):
        if float(price_list[j]) >= max_price:
            max_price = float(price_list[j])
    return max_price


# lowest_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def lowest_price(data, start_date, end_date):
    price_list = []

    File_Start_epoch = 1430179200
    File_End_epoch = 1602979200

    # convert from time to epoch timestamp
    try:
        start_epoch = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    except ValueError:
        print("Error: invalid date value")
        sys.exit()

    # custom exception to catch those start larger than end
    try:
        # check error condition
        if end_epoch < start_epoch:
            raise MyException("Error: end date must be larger than start date")
    except MyException as e:
        print(str(e))
        sys.exit()

    # custom exception to catch those outbound the date
    try:
        # check error condition
        if end_epoch > File_End_epoch or start_epoch > File_End_epoch \
                or end_epoch < File_Start_epoch or start_epoch < File_Start_epoch:
            raise MyException("Error: date value is out of range")
    except MyException as e:
        print(str(e))
        sys.exit()

    # find those satisfying the periods
    try:
        for i in range(len(data)):
            row = data[i]
            if start_epoch <= int(row['time']) <= end_epoch:
                price_list.append(row['low'])
    except KeyError:
        print("Error: requested column is missing from dataset")
        sys.exit()

    # find the lowest value and return the value
    min_price = float(price_list[0])
    for j in range(len(price_list)):
        if float(price_list[j]) <= min_price:
            min_price = float(price_list[j])
    return min_price


# max_volume(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def max_volume(data, start_date, end_date):
    volume_list = []
    File_Start_epoch = 1430179200
    File_End_epoch = 1602979200
    # convert from time to epoch timestamp
    try:
        start_epoch = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    except ValueError:
        print("Error: invalid date value")
        sys.exit()

    # custom exception to catch those start larger than end
    try:
        # check error condition
        if end_epoch < start_epoch:
            raise MyException("Error: end date must be larger than start date")
    except MyException as e:
        print(str(e))
        sys.exit()

    # custom exception to catch those outbound the date
    try:
        # check error condition
        if end_epoch > File_End_epoch or start_epoch > File_End_epoch \
                or end_epoch < File_Start_epoch or start_epoch < File_Start_epoch:
            raise MyException("Error: date value is out of range")
    except MyException as e:
        print(str(e))
        sys.exit()

    # find those satisfying the periods
    try:
        for i in range(len(data)):
            row = data[i]
            if start_epoch <= int(row['time']) <= end_epoch:
                volume_list.append(row['volumefrom'])
    except KeyError:
        print("Error: requested column is missing from dataset")
        sys.exit()

    # find the max value and return
    Maxvolume = float(volume_list[0])
    for j in range(len(volume_list)):
        if float(volume_list[j]) >= Maxvolume:
            Maxvolume = float(volume_list[j])
    return Maxvolume


# best_avg_price(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def best_avg_price(data, start_date, end_date):
    price_list = []
    File_Start_epoch = 1430179200
    File_End_epoch = 1602979200
    # convert from time to epoch timestamp
    try:
        start_epoch = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    except ValueError:
        print("Error: invalid date value")
        sys.exit()

    # custom exception to catch those start larger than end
    try:
        # check error condition
        if end_epoch < start_epoch:
            raise MyException("Error: end date must be larger than start date")
    except MyException as e:
        print(str(e))
        sys.exit()

    # custom exception to catch those outbound the date
    try:
        # check error condition
        if end_epoch > File_End_epoch or start_epoch > File_End_epoch \
                or end_epoch < File_Start_epoch or start_epoch < File_Start_epoch:
            raise MyException("Error: date value is out of range")
    except MyException as e:
        print(str(e))
        sys.exit()

    # find those satisfying the periods
    try:
        for i in range(len(data)):
            row = data[i]
            if start_epoch <= int(row['time']) <= end_epoch:
                volume_from = float(row['volumefrom'])
                volume_to = float(row['volumeto'])
                avg_price = volume_to / volume_from
                price_list.append(avg_price)
    except KeyError:
        print("Error: requested column is missing from dataset")
        sys.exit()

    # find the max value and return
    max_avg_price = price_list[0]
    for j in range(len(price_list)):
        if float(price_list[j]) >= max_avg_price:
            max_avg_price = float(price_list[j])
    return max_avg_price


# moving_average(data, start_date, end_date) -> float
# data: the data from a csv file
# start_date: string in "dd/mm/yyyy" format
# start_date: string in "dd/mm/yyyy" format
def moving_average(data, start_date, end_date):
    Total = 0
    DayNumber = 0
    File_Start_epoch = 1430179200
    File_End_epoch = 1602979200
    # convert from time to epoch timestamp
    try:
        start_epoch = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    except ValueError:
        print("Error: invalid date value")
        sys.exit()

    # custom exception to catch those start larger than end
    try:
        # check error condition
        if end_epoch < start_epoch:
            raise MyException("Error: end date must be larger than start date")
    except MyException as e:
        print(str(e))
        sys.exit()

    # custom exception to catch those outbound the date
    try:
        # check error condition
        if end_epoch > File_End_epoch or start_epoch > File_End_epoch \
                or end_epoch < File_Start_epoch or start_epoch < File_Start_epoch:
            raise MyException("Error: date value is out of range")
    except MyException as e:
        print(str(e))
        sys.exit()

    # find those satisfying the periods and return the value required
    try:
        for i in range(len(data)):
            row = data[i]
            if start_epoch <= int(row['time']) <= end_epoch:
                volume_from = float(row['volumefrom'])
                volume_to = float(row['volumeto'])
                avg_price = volume_to / volume_from
                Total += avg_price
                DayNumber += 1
    except KeyError:
        print("Error: requested column is missing from dataset")
        sys.exit()
    if DayNumber != 0:
        return Total / DayNumber


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program

    # Example variable initialization
    # data is always the cryptocompare_btc.csv read in using a DictReader
    # Check if the csv. file exists in the dict path
    try:
        data = []
        with open("cryptocompare_btc.csv", "r") as f:
            reader = csv.DictReader(f)
            data = [r for r in reader]
    except FileNotFoundError:
        print("Error: dataset not found")
        sys.exit()



    # test
    Start_Date = "01/01/2016"
    End_Date = "01/01/2016"
    try:
        print("highest_price = ", highest_price(data, Start_Date, End_Date))
        print("lowest_price = ", lowest_price(data, Start_Date, End_Date))
        print("max_volume = ", max_volume(data, Start_Date, End_Date))
        print("best_avg_price = ", best_avg_price(data, Start_Date, End_Date))
        print("moving_average = ", moving_average(data, Start_Date, End_Date))
    except IndexError:
        print()

    pass
