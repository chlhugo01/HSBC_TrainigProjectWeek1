import account
import customer
import transaction as tr
from datetime import datetime

class transfunctions:
    
    def __init__(self):
        self.id=0
    
    
    
    def getTransaction(self,account):
            
            # Check if the transaction list is empty
            if len(account.transactionlist) == 0:
                print("No transactions found.")
            else:
            # Get the last ten transactions or all transactions if less than ten
                last_ten_transactions = account.transactionlist[-10:]

            # Loop through the transactions
            for transaction in last_ten_transactions:
                print("Date:", transaction.date)
                print("ID:", transaction.id)
                print("Amount:", transaction.amount)
                print("CR/DR:", transaction.crdr)
                print("Balance:", transaction.balance)
                print("Description:", transaction.description)
                print("-----------------------")

    def showbalance(self,account):
        return int(account.balance)
    
    def withdraw(self,amount,account):
        if amount > account.balance:
            print("Not enough balance")
            return False
        account.balance  -= amount
        traid = str(self.id) + str(datetime.now())
        account.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"dr",account.balance, "withdrawal"))
        return True


    def deposit(self,amount,account):
        
        account.balance += amount
        traid = str(self.id) + str(datetime.now())
        account.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"cr",account.balance, "deposit"))
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