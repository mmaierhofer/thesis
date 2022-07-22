from time import time
from numpy import append
from tokens import tokens
from Transaction import Transaction
from Dao import Dao

import csv


def in_euro(amount, usedToken):
    amount_in_euros = 0
    for token in tokens:
        if token["name"] == usedToken:
            amount_in_euros = float(amount) * token["EUR"]
    return amount_in_euros


def get_amount_out(transactions):

    token_history = []

    for transaction in transactions:
        if(transaction.type is not "Rage Quit"):
            if len(token_history) > 0:
                newValue = int(transaction.amount_out) + \
                    int(token_history[len(token_history) - 1])
            elif len(token_history) == 0:
                newValue = int(transaction.amount_out)
            elif len(token_history) > 0:
                newValue = int(token_history[len(token_history) - 1])
            else:
                newValue = 0

            token_history.append(newValue)

    return token_history


def get_amount_in(transactions):

    token_history = []

    for transaction in transactions:
        if(transaction.type is not "Rage Quit"):
            if len(token_history) > 0:
                newValue = int(transaction.amount_in) + \
                    int(token_history[len(token_history) - 1])
            elif len(token_history) == 0:
                newValue = int(transaction.amount_in)
            elif len(token_history) > 0:
                newValue = int(token_history[len(token_history) - 1])
            else:
                newValue = 0

            token_history.append(newValue)

    return token_history


def get_amount_members(transactions):

    member_history = []
    timestamps = []

    for transaction in transactions:

        if len(member_history) > 0:
            if int(transaction.amount_in) > 0:
                member_history.append(
                    member_history[len(member_history) - 1] + 1)
            elif transaction.type == "Rage Quit" and transaction.date not in timestamps:
                member_history.append(
                    member_history[len(member_history) - 1] - 1)
                timestamps.append(transaction.date)
            else:
                member_history.append(
                    member_history[len(member_history) - 1])
        else:
            if int(transaction.amount_in) > 0:
                member_history.append(1)
            else:
                member_history.append(0)

    return member_history


def get_daos(files):
    daos = []
    for file in files:
        transactions = []

        with open(f'./data/{file}.csv') as csv_file:
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
            print(f'Processed {line_count} lines for {file}.')

        dao = Dao(file, transactions)
        daos.append(dao)

    return daos


def get_all_members(daos):

    members = []

    for dao in daos:
        for transaction in dao.transactions:
            if(transaction.applicant is not "" and transaction.type is not "Rage Quit"):
                print(transaction.type)
                members.append(transaction.applicant)

    return members


def get_rage_quits(transactions):
    rage_quits = []

    timestamps = []

    for transaction in transactions:
        if len(rage_quits) > 0:
            if(transaction.type == "Rage Quit" and transaction.date not in timestamps):
                timestamps.append(transaction.date)
                rage_quits.append(rage_quits[len(rage_quits)-1] + 1)
            else:
                rage_quits.append(rage_quits[len(rage_quits)-1] + 0)
        else:
            if(transaction.type == "Rage Quit"):
                timestamps.append(transaction.date)
                rage_quits.append(1)
            else:
                rage_quits.append(0)
    return rage_quits
