import sys
import matplotlib.pyplot as plt
import csv
import time
import calendar

"""
    Part D
    Please provide definitions for the following class and functions
"""


class MyException(Exception):

    # Exception message set by value
    def __init__(self, value):
        self.parameter = value

    # Exception message to be printed
    def __str__(self):
        return self.parameter


# Class Investment:
# Instance variables
#	start date
#	end date
#	data 
# Functions
#	highest_price(data, start_date, end_date) -> float
#	lowest_price(data, start_date, end_date) -> float
#	max_volume(data, start_date, end_date) -> float
#	best_avg_price(data, start_date, end_date) -> float
#	moving_average(data, start_date, end_date) -> float


class Investment:
    # Construct
    def __init__(self, data, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

        # choose the satisfying data
        newdata = []
        start_epoch = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
        end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
        for i in range(len(data)):
            row = data[i]
            if start_epoch <= int(row['time']) <= end_epoch:
                newdata.append(row)
        self.data = newdata

    def highest_price(self, data=[], start_date='', end_date=''):
        # Use Instance variables
        data = self.data
        start_date = self.start_date
        end_date = self.end_date

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

    def lowest_price(self, data=[], start_date='', end_date=''):
        # Use Instance variables
        data = self.data
        start_date = self.start_date
        end_date = self.end_date

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

    def max_volume(self, data=[], start_date='', end_date=''):
        # Use Instance variables
        data = self.data
        start_date = self.start_date
        end_date = self.end_date

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

    def best_avg_price(self, data=[], start_date='', end_date=''):
        # Use Instance variables
        data = self.data
        start_date = self.start_date
        end_date = self.end_date

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

    def moving_average(self, data=[], start_date='', end_date=''):
        # Use Instance variables
        data = self.data
        start_date = self.start_date
        end_date = self.end_date

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

    pass


# build regression model
def regression(investment):
    new_Data = investment.data
    # convert str date to epoch
    start_date = investment.start_date
    end_date = investment.end_date
    start_epoch = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))

    avg_price_list = []
    time_epoch_list = []
    Total_avg_price = 0
    for i in range(len(new_Data)):
        row = new_Data[i]
        if start_epoch <= int(row['time']) <= end_epoch:
            each_epoch = float(row['time'])
            time_epoch_list.append(each_epoch)
            volume_from = float(row['volumefrom'])
            volume_to = float(row['volumeto'])
            avg_price = volume_to / volume_from
            Total_avg_price += avg_price
            avg_price_list.append(avg_price)
    # calculate the average valur for the linear regression model
    avg_y = sum(avg_price_list) / len(avg_price_list)
    avg_x = sum(time_epoch_list) / len(time_epoch_list)

    # build the regression model
    summary = 0
    var = 0
    for j in range(len(avg_price_list)):
        summary += (avg_price_list[j] - avg_y) * (time_epoch_list[j] - avg_x)
        var += (time_epoch_list[j] - avg_x) * (time_epoch_list[j] - avg_x)
    m = summary / var
    b = avg_y - m * avg_x
    return m, b


# predict_next_average(investment) -> float
# investment: Investment type
def predict_next_average(investment):
    m, b = regression(investment)
    # y = mx+b, here y is the next average and x is the next date
    end_date = investment.end_date
    end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))
    next_epoch = end_epoch + 86400
    next_avg = m * next_epoch + b
    return next_avg


# classify_trend(investment) -> str
# investment: Investment type
def classify_trend(investment):
    new_Data = investment.data
    # convert str date to epoch
    start_date = investment.start_date
    end_date = investment.end_date
    start_epoch = calendar.timegm(time.strptime(start_date, "%d/%m/%Y"))
    end_epoch = calendar.timegm(time.strptime(end_date, "%d/%m/%Y"))

    daily_high_list = []
    daily_low_list = []
    time_epoch_list = []
    for i in range(len(new_Data)):
        row = new_Data[i]
        if start_epoch <= int(row['time']) <= end_epoch:
            each_epoch = float(row['time'])
            time_epoch_list.append(each_epoch)
            daily_high = float(row['high'])
            daily_low = float(row['low'])
            daily_high_list.append(daily_high)
            daily_low_list.append(daily_low)

    # build regression model for daily_high
    avg_y = sum(daily_high_list) / len(daily_high_list)
    avg_x = sum(time_epoch_list) / len(time_epoch_list)
    summary_high = 0
    var_high = 0
    for j in range(len(daily_high_list)):
        summary_high += (daily_high_list[j] - avg_y) * (time_epoch_list[j] - avg_x)
        var_high += (time_epoch_list[j] - avg_x) * (time_epoch_list[j] - avg_x)
    m = summary_high / var_high

    # build regression model for daily_low
    avg_y1 = sum(daily_low_list) / len(daily_low_list)
    avg_x1 = sum(time_epoch_list) / len(time_epoch_list)
    summary_low = 0
    var_low = 0
    for j in range(len(daily_low_list)):
        summary_low += (daily_low_list[j] - avg_y1) * (time_epoch_list[j] - avg_x1)
        var_low += (time_epoch_list[j] - avg_x1) * (time_epoch_list[j] - avg_x1)
    m1 = summary_low / var_low

    result = ''
    if (m1 > 0) & (m > 0):
        result = 'increasing'
    elif (m1 < 0) & (m < 0):
        result = 'decreasing'
    else:
        result = 'other'

    return result


# Replace the body of this main function for your testing purposes
if __name__ == "__main__":
    # Start the program
    data = []
    with open("cryptocompare_btc.csv", "r") as f:
        reader = csv.DictReader(f)
        data = [r for r in reader]

    # test
    start_date = '08/12/2016'
    end_date = '11/12/2016'
    investment = Investment(data, start_date, end_date)
    print(predict_next_average(investment))
    print(classify_trend(investment))
    pass
