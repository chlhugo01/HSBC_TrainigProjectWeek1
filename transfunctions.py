import account as ac
import customer as ct
import transaction as tr
from datetime import datetime
import database as db


def getTransaction(account):
        
        # Check if the transaction list is empty
        if len(account.get_transactionlist()) == 0:
            print("No transactions found.")
        else:
        # Get the last ten transactions or all transactions if less than ten
            last_ten_transactions = account.get_transactionlist()[-10:]

        # Loop through the transactions
            for transaction in last_ten_transactions:
                print("Date:", transaction.get_date())
                print("ID:", transaction.get_id())
                print("Amount:", transaction.get_amount())
                print("CR/DR:", transaction.get_crdr())
                print("Balance:", transaction.get_balance())
                print("Description:", transaction.get_description())
                print("-----------------------")

def showbalance(connection,AccID):
    #print(account.balance)
    query1 = 'Select * from account where AccID=' + str(AccID)
    result = db.execute_read_query(connection, query1)
    return result[0]

def withdraw(connection,amount,balance,AccID):
    newbalance = balance-amount
    print(newbalance)
    query1 = 'update account set balance = ' + str(newbalance) +' where AccID = ' + str(AccID)
   # Fix Bug query2 = 'insert into transaction(TrID,Amount,CRDR,Balance,Description,AccID) VALUES' + '(1,amount,DR,balance-amount,Withdraw,AccID)'
    db.execute_read_query(connection, query1)
    db.execute_read_query(connection, query2)

    return True


def deposit(amount,account):
    accbal = account.get_balance()
    accbal += amount
    account.set_balance(accbal)
    traid = str(account.get_id()) + str(datetime.now())
    account.set_transactionList(tr.transaction(datetime.now(),traid,amount,"cr",account.get_balance(), "deposit"))
    return True
    

def transfer(amount,sender,recip):
    if amount>0:
        senbal = sender.get_balance()
        if amount > senbal:
            print("Not enough balance")
            return False
        senbal  -= amount
        sender.set_balance(senbal)
        traid = str(sender.get_id()) + str(datetime.now())
        sender.set_transactionList(tr.transaction(datetime.now(),traid,amount,"dr",sender.get_balance(), "transfer (sender)"))
        transfer(-abs(amount),sender,recip)
    else:
        rec = recip.get_balance()
        rec  += amount
        recip.set_balance(rec)
        traid = str(recip.get_id()) + str(datetime.now())
        recip.set_transactionList(tr.transaction(datetime.now(),traid,amount,"cr",recip.get_balance(), "transfer (recipient)"))
    return True