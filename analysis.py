from audioop import reverse
from matplotlib import pyplot as plt
from utils import get_all_members, get_amount_members, get_amount_in, get_amount_out, get_daos, get_num_participation, get_proposals_in, get_rage_quits, in_euro

import numpy as np

names = [
    #"DAOhaus CCO",
    #"Diamond Bank",
    #"Game Mine Alliance",
    #"HausDAO Warcamp",
    #"Moloch Rises",
    #"RaidBroodBeer DAO",
    #"Raid Guild",
    "The LAO"
]

files = [
    # "DAOhausCCO",
    # "DiamondBank",
    # "GameMineAlliance",
    # "HausDAOWarcamp",
    # "MetaCartelVentures",
    # "MolochDAO",
    # "RaidBroodBeerDAO",
    # "RaidGuild",
    "TheLAO"
]

daos = get_daos(files)

members = get_all_members(daos)

in_euro(200, "MVC202")


def scatter():

    fig, ax = plt.subplots()

    x = [105, 20, 36, 38, 85, 74, 148, 78]
    part_in = [3, 10, 18, 132, 157, 4, 100, 93]

    part_out = [2, 28, 33, 1, 140, 11, 84, 31]

    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:olive',
              'tab:red', 'tab:purple', 'tab:pink']

    for idx, color in enumerate(colors):
        plt.scatter(x[idx], part_in[idx], c=color, alpha=0.5,
                    label=names[idx])
    plt.xlabel("Members")
    plt.ylabel("Participation")
    plt.legend(loc='upper right')

    # plt.show()

    # plt.grid()


    # plot data
# scatter()
for idx, dao in enumerate(daos):

    # print(get_num_participation(dao.transactions))
    # activities = get_amount_members(dao.transactions.reverse())
    #incoming = get_amount_in(dao.transactions)
    #proposals = get_proposals_in(dao.transactions)
    outgoing = get_amount_out(dao.transactions)
    #rage_quits = get_rage_quits(dao.transactions)

    plt.plot(outgoing[1], outgoing[0],  label=names[idx])
    #plot(outgoing, "Time", "Tokens Outgoing")

    #plt.plot(proposals[1], proposals[0],  label=names[idx])

    print(names[idx])
    # print(proposals[0][0])

# create data

plt.legend(loc='upper left')

plt.xlabel("Time")
plt.ylabel("Value of Tokens spent")
plt.show()
