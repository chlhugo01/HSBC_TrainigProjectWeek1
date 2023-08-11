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
        return True


    def deposit(self,amount):
        
        self.balance  += amount
        traid = str(self.id) + str(datetime.now())
        self.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"cr",self.balance, "deposit"))
        return True
        
    
    def transfer(self,amount,recip):
        if amount>0:
            if amount > self.balance:
                print("Not enough balance")
                return False
            self.balance  -= amount
            traid = str(self.id) + str(datetime.now())
            self.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"dr",self.balance, "transfer"))
            recip.transfer(-abs(amount),self)
        else: 
            self.balance  += amount
            traid = str(self.id) + str(datetime.now())
            self.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"cr",self.balance, "transfer"))
        return True

