from datetime import datetime
import transaction as tr

class customer:

    def __init__(self, id, name, balance):
        self.transactionlist = []
        self.id = id
        self.name = name
        self.balance = balance
    
    def getTransaction(self):
        
        # Check if the transaction list is empty
        if len(self.transactionlist) == 0:
            print("No transactions found.")
        else:
        # Get the last ten transactions or all transactions if less than ten
            last_ten_transactions = self.transactionlist[-10:]

        # Loop through the transactions
        for transaction in last_ten_transactions:
            print("Date:", transaction.date)
            print("ID:", transaction.id)
            print("Amount:", transaction.amount)
            print("CR/DR:", transaction.crdr)
            print("Balance:", transaction.balance)
            print("Description:", transaction.description)
            print("-----------------------")

    def showbalance(self):
        return int(self.balance)
    
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
            self.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"dr",self.balance, "transfer (sender)"))
            recip.transfer(-abs(amount),self)
        else: 
            self.balance  += amount
            traid = str(self.id) + str(datetime.now())
            self.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"cr",self.balance, "transfer (recipient)"))
        return True

