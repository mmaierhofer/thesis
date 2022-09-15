from audioop import reverse
from matplotlib import pyplot as plt
from utils import get_amount_in, get_amount_out, get_daos, get_num_participation, get_proposals_in, get_rage_quits

import numpy as np

## Names for the labels of the DAO forks
## represented in the 
names = [
    "DAOhaus CCO",
    "Diamond Bank",
    "Game Mine Alliance",
    "HausDAO Warcamp",
    "MetaCartel Ventures"
    "Moloch Rises",
    "RaidBroodBeer DAO",
    "Raid Guild",
    "The LAO"
]

## Filenames important for importing
## transactional data from the forks
## further down
fileNames = [
    "DAOhausCCO",
    "DiamondBank",
    "GameMineAlliance",
    "HausDAOWarcamp",
    "MetaCartelVentures",
    "MolochDAO",
    "RaidGuild",
    "TheLAO"
]

## import daos from fileNames
daos = get_daos(fileNames)



## Scatterplot used for looking at the relation between
## members of forks and their participation in order to
## provide insights on whether popularity of a projects
## influences participation. 
def scatter():

    fig, ax = plt.subplots()

    ## Active Members of the forks
    members = [105, 20, 36, 38, 85, 74, 148, 78]

    # Participation within the project for each DAO
    part_in = [3, 10, 18, 132, 157, 4, 100, 93]

    # Participation with the ecosystem for each DAO
    part_out = [2, 28, 33, 1, 140, 11, 84, 31]

    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:olive',
              'tab:red', 'tab:purple', 'tab:pink']

    for idx, color in enumerate(colors):
        plt.scatter(members[idx], part_in[idx], c=color, alpha=0.5,
                    label=names[idx])
    plt.xlabel("Members")
    plt.ylabel("Participation")
    plt.legend(loc='upper right')



## Iterate over DAO forks in order
## to create different plots to 
## get insights on the transactional data
for idx, dao in enumerate(daos):

    # incoming = get_amount_in(dao.transactions)
    # proposals = get_proposals_in(dao.transactions)
    # outgoing = get_amount_out(dao.transactions)
    rage_quits = get_rage_quits(dao.transactions)

    plt.plot(rage_quits[1], rage_quits[0],  label=names[idx])
    #plt.plot(proposals[1], proposals[0],  label=names[idx])
    #plt.plot(incoming[1], incoming[0],  label=names[idx])
    #plt.plot(outgoing[1], outgoing[0],  label=names[idx])


# create data

## create plots

plt.legend(loc='upper left')
plt.xlabel("Time")
plt.ylabel("Ragequits")
plt.show()
