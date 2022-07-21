from matplotlib import pyplot as plt
from utils import get_amount_out_history
from Transaction import Transaction

import csv
import numpy as np

transactions = []

with open('./data/metaCartel.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            transaction = Transaction(
                row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            transactions.append(transaction)
    print(f'Processed {line_count} lines.')

print(get_amount_out_history(transactions))

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
