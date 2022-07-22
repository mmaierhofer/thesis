from audioop import reverse
from matplotlib import pyplot as plt
from utils import get_all_members, get_amount_members, get_amount_in, get_amount_out, get_daos, get_rage_quits

import numpy as np

files = [
    "theLao",
    "metaCartel",
    "MetaGammaDeltaDao"
]

daos = get_daos(files)

members = get_all_members(daos)

membersSet = set(members)

print(len(members))
print(len(membersSet))

# plot data
for dao in daos:
    activities = get_amount_members(dao.transactions)
    incoming = get_amount_in(dao.transactions)
    outgoing = get_amount_out(dao.transactions)
    rage_quits = get_rage_quits(dao.transactions)

    fig, ax = plt.subplots()
    ax.plot(activities, rage_quits)

    ax.set(xlabel='Incoming Activities', ylabel='Rage Quits',
           title=f'{dao.name}')
    ax.grid()

    fig.savefig("test.png")
    plt.show()
