import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Data/2863477.csv'

with open(filename, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for position, title in enumerate(header):
        print(position, title)

    highs = []
    lows = []
    dates = []

    for temp in reader:
        try:
            high = int(temp[2])
            low = int(temp[3])
        except IndexError:
            continue
        else:
            highs.append(high)
            current_date = datetime.strptime(temp[1], '%Y-%m-%d')
            dates.append(current_date)
            lows.append(low)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    plt.plot(dates, highs, label='highs', color='red')
    plt.plot(dates, lows, label='lows', color='blue')
    plt.title('Texas Snow Storm Daily Highs and Lows \n2021', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
