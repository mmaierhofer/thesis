def get_amount_out_history(transactions):

    token_history = []

    for transaction in transactions:

        if (len(token_history) > 0):
            newValue = int(transaction.amount_out) + \
                int(token_history[len(token_history) - 1])
        else:
            newValue = int(transaction.amount_out)

        token_history.append(newValue)

    return token_history
