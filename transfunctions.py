import account
import customer
import transaction as tr
from datetime import datetime


def getTransaction(account):
        
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

def showbalance(account):
    #print(account.balance)
    return str(account.balance)

def withdraw(amount,account):
    if amount > account.balance:
        print("Not enough balance")
        return False
    account.balance  -= amount
    traid = str(self.id) + str(datetime.now())
    account.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"dr",account.balance, "withdrawal"))
    return True


def deposit(amount,account):
    
    account.balance += amount
    traid = str(account.id) + str(datetime.now())
    account.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"cr",account.balance, "deposit"))
    return True
    

def transfer(amount,sender,recip):
    if amount>0:
        if amount > sender.balance:
            print("Not enough balance")
            return False
        sender.balance  -= amount
        traid = str(account.id) + str(datetime.now())
        sender.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"dr",sender.balance, "transfer (sender)"))
        recip.transfer(-abs(amount),sender)
    else: 
        recip.balance  += amount
        traid = str(recip.id) + str(datetime.now())
        recip.transactionlist.append(tr.transaction(datetime.now(),traid,amount,"cr",recip.balance, "transfer (recipient)"))
    return True