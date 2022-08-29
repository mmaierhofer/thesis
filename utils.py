import json
from time import time
from numpy import append
from tokens import tokens
from Transaction import Transaction
from Dao import Dao
from datetime import datetime
import requests
import csv

api_key = "cf5d72df5d2ab38704096fba561cfcd191ea89bbcba92c4890562c8fa896fdf2"


def in_euro(amount, usedToken):
    if "MCV" in usedToken:
        return float(0)
    for token in tokens:
        if token["name"] == usedToken:
            amm = float(amount) * token["DOL"]
            return float(amount) * token["DOL"]


def get_amount_out(transactions):

    token_history = []

    transactions.reverse()

    times = []

    for transaction in transactions:
        if(transaction.type != "Rage Quit"):
            if len(token_history) > 0:
                newValue = float(in_euro(transaction.amount_out, transaction.token)) + \
                    float(token_history[len(token_history) - 1])
            elif len(token_history) == 0:
                newValue = float(
                    in_euro(transaction.amount_out, transaction.token))
            elif len(token_history) > 0:
                newValue = float(token_history[len(token_history) - 1])
            else:
                newValue = 0

            if float(transaction.amount_out) > 0:
                print(in_euro(transaction.amount_out, transaction.token))
                print(datetime.fromtimestamp(int(transaction.date)))
                print(transaction.title)

            timestamp = int(transaction.date)
            times.append(timestamp)
            token_history.append(
                newValue)

    for idx, time in enumerate(times):
        times[idx] = datetime.fromtimestamp(time)

    print(token_history[len(token_history)-1])

    return [token_history, times]


def get_num_participation(transactions):

    count = 0

    for transaction in transactions:
        if (int)(transaction.amount_out) > 0:
            count += 1
    return count


def get_amount_in(transactions):

    token_history = []

    times = []

    for transaction in transactions:
        if(transaction.type is "proposal"):
            if len(token_history) > 0:
                newValue = float(in_euro(transaction.amount_in, transaction.token)) + \
                    float(token_history[len(token_history) - 1])
            elif len(token_history) == 0:
                newValue = float(
                    in_euro(transaction.amount_in, transaction.token))
            elif len(token_history) > 0:
                newValue = float(token_history[len(token_history) - 1])
            else:
                newValue = 0
        token_history.append(newValue)

        # token_history.append((float(transaction.amount_in)))
        timestamp = int(transaction.date)
        times.append(timestamp)

    for idx, time in enumerate(times):
        times[idx] = datetime.fromtimestamp(time)

    token_history.reverse()

    return [token_history, times]


def get_proposals_in(transactions):

    history = []

    transactions.reverse()

    times = []

    for transaction in transactions:
        if(transaction.type != "Rage Quit" and transaction.type != "Tokens Collected" and float(transaction.amount_in) > 0):
            if len(history) > 0:
                newValue = 1 + history[len(history) - 1]
            elif len(history) == 0:
                newValue = 1
            elif len(history) > 0:
                newValue = history[len(history) - 1]
            else:
                newValue = 0
            history.append(newValue)

            # token_history.append((float(transaction.amount_in)))
            timestamp = int(transaction.date)
            times.append(timestamp)

    for idx, time in enumerate(times):
        times[idx] = datetime.fromtimestamp(time)

    times.append(datetime.fromtimestamp(1659304800))
    history.append(history[len(history) - 1])

    return [history, times]


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

        with open(f'./data/final/{file}.csv') as csv_file:
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
                    # transactions.reverse()
            print(f'Processed {line_count} lines for {file}.')

        dao = Dao(file, transactions)
        daos.append(dao)

    return daos


def get_all_members(daos):

    members = []

    for dao in daos:
        for transaction in dao.transactions:
            if(transaction.applicant != "" and transaction.type != "Rage Quit"):
                members.append(transaction.applicant)

    return members


def get_rage_quits(transactions):
    rage_quits = []

    timestamps = []

    times = []

    for transaction in transactions:
        if len(rage_quits) > 0:
            if(transaction.type == "Rage Quit" and transaction.date not in timestamps):
                timestamps.append(transaction.date)
                rage_quits.append(rage_quits[len(rage_quits)-1] + 1)
                timestamp = int(transaction.date)
                times.append(timestamp)
            else:
                """rage_quits.append(rage_quits[len(rage_quits)-1] + 0)"""
        else:
            if(transaction.type == "Rage Quit"):
                timestamps.append(transaction.date)
                rage_quits.append(1)
                timestamp = int(transaction.date)
                times.append(timestamp)
            else:
                """rage_quits.append(0)"""

    for idx, time in enumerate(times):
        times[idx] = datetime.strptime(datetime.strftime(
            datetime.fromtimestamp(time), "%m-%Y"), "%m-%Y")

    rage_quits.insert(0, 0)
    rage_quits.append(rage_quits[len(rage_quits)-1])
    times.insert(0, datetime.fromtimestamp(1659304800))
    times.append(datetime.fromtimestamp(1583017200))

    rage_quits.reverse()

    print(rage_quits[0])
    return [rage_quits, times]
