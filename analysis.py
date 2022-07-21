from audioop import reverse
from matplotlib import pyplot as plt
from utils import get_amount_members, get_amount_out_history
from Transaction import Transaction

import csv
import numpy as np

transactions = []

with open('./data/theLao.csv') as csv_file:
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
            transactions.reverse()
    print(f'Processed {line_count} lines.')


# Data for plotting
t = get_amount_members(transactions)
s = get_amount_out_history(transactions)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='Members', ylabel='Tokens spent',
       title='Participation Activities and Token History')
ax.grid()

fig.savefig("test.png")
plt.show()
