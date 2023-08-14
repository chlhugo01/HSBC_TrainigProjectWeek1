from datetime import datetime
import transaction as tr

class account:

    def __init__(self, id, name, balance):
        self.transactionlist = []
        self.id = id
        self.name = name
        self.balance = balance

