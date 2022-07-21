class Transaction:
    def __init__(self, date, type, shares, loot, applicant, title, token, amount_in, amount_out):
        self.date = date
        self.type = type
        self.shares = shares
        self.loot = loot
        self.applicant = applicant
        self.title = title
        self.token = token
        self.amount_in = amount_in
        self.amount_out = amount_out
