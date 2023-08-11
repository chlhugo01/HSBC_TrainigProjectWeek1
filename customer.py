from datetime import datetime
import transaction as tr

class customer:

    def __init__(self, id, name, balance):
        self.transactionlist = []
        self.id = id
        self.name = name
        self.balance = balance
    def showbalance(self):
        return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
            print("Not enough balance")
            return False
        self.balance  -= amount
        traid = str(self.id) + str(datetime.now())
        self.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"dr",self.balance, "withdrawal"))


    def deposit(self):
        return True
    def transfer(self):
        return True

