from time import time
from numpy import append
from tokens import tokens


def in_euro(amount, usedToken):
    amount_in_euros = 0
    for token in tokens:
        if token["name"] == usedToken:
            amount_in_euros = float(amount) * token["EUR"]
    return amount_in_euros


def get_amount_out_history(transactions):

    token_history = []

    for transaction in transactions:

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
