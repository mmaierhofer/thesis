from audioop import reverse
from matplotlib import pyplot as plt
from utils import get_all_members, get_amount_members, get_amount_in, get_amount_out, get_daos, get_rage_quits, get_rage_quits_by_date

import numpy as np

files = [
    "theLao",
    "metaCartel"
    # "molochDAO"
]

daos = get_daos(files)

members = get_all_members(daos)

membersSet = set(members)

print(len(members))
print(len(membersSet))

# plot data
for dao in daos:

    rage_quits_date = get_rage_quits_by_date(dao.transactions)

    ##activities = get_amount_members(dao.transactions.reverse())
    incoming = get_amount_in(dao.transactions)
    outgoing = get_amount_out(dao.transactions)
    rage_quits = get_rage_quits(dao.transactions)

    fig, ax = plt.subplots()
    ax.plot(outgoing[1], outgoing[0])

    ax.set(xlabel='Time', ylabel='Token Outgoing',
           title=f'{dao.name}')
    ax.grid()

    fig.savefig("test.png")
    plt.show()
