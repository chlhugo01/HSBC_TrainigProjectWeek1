import account as ac
import transaction as tr
import transfunctions as trfun
import customer as ct
import database as db
import mysql.connector
from mysql.connector import Error

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def day_1():
    connection = db.create_connection('127.0.0.1', 'bankserver', 'root', 'Clch2811!')
    '''
    query = """
            SELECT first_name, last_name, count(*) films
            FROM actor AS a
            JOIN film_actor AS fa USING (actor_id)
            GROUP BY actor_id, first_name, last_name
            ORDER BY films DESC
        """
    films = db.execute_read_query(connection, query)

    for film in films:
        print(film)


    cuslist = [{"id": 1, "name": "Hugo",'email':"hugo@gmail.com",'address':'hsbc' },
               {"id": 2, "name": "Cora", 'email':"Cora@gmail.com",'address':'hsbc'},
               {"id": 3, "name": "John", 'email':"John@gmail.com",'address':'hsbc'},
               {"id": 4, "name": "Alvin", 'email':"Alvin@gmail.com",'address':'hsbc'},
               {"id": 5, "name": "Bell",'email':"Bell@gmail.com",'address':'hsbc' }
               ]
    cclasslist = []

    for i in range(0,len(cuslist)):
        temp = ct.customer(i+1 , cuslist[i]["name"],cuslist[i]['email'],cuslist[i]['address'])
        temp.set_accountList(ac.account(i+1, "Savings", 0))   # account id same as customer id
        cclasslist.append(temp)

    '''
    found=False
    cus = input('Please enter your customer id:')
    query1 = 'Select * from ACCOUNT where CusID=' + str(cus)

    account = db.execute_read_query(connection, query1)
    for i in range(len(account)):
        print(str(account[i][0])+ " " + str(account[i][1]))

    print("Please select an account")

    AccID=input()
    
    
    
    
    
    while 1:
        choice = int(input('''Welcome to the bank system?
          Please state your action
          - 1: Show Balance
          - 2: Withdraw Money
          - 3: Deposit Money
          - 4: Transfer Funds
          - 5: Display last 10 Transactions
          - 6: Quit program
          ''' ))

        if choice == 1:
            print("Your balance:  " + str(trfun.showbalance(connection,AccID)[2]))
            #print("Your balance:  " + str(trfun.showbalance(sdac)))
        elif choice == 2:

            withdrawamount = int(input("How much you want to withdraw:"))
            if withdrawamount <= int(account[0][2]):
                trfun.withdraw(connection,withdrawamount,int(account[0][2]),AccID)
            else:
                print("Your withdrawal is not approved, not enough balance")
        elif choice == 3:
            
            depositamount = int(input("How much you want to deposit"))
            trfun.deposit(depositamount,sdac)
            print("Your balance:  " + str(trfun.showbalance(sdac)))
            print("You withdraw" + str(depositamount))

        elif choice==4:
            
            
            recip=input("Who do you want to transfer to?")
            
            found=False
                    
            for i in range(len(cclasslist)):
                if(cclasslist[i].get_name() == recip):
                    recip = cclasslist[i]
                    found=True
                    break
                
            if not found:
                print("no customer found")
                exit()
                
            print("Please select an account:")
            
            racclist=recip.get_accountList()
            
            for i in range(len(racclist)):
                
                print(str(i)+": "+racclist[i].get_name())
            
            accid=input()
            recipacc = racclist[int(accid)]
            

            transferamount = int(input("How much you want to transfer"))
            
            trfun.transfer(transferamount,sdac,recipacc)
            
            print("Your balance:  " + str(trfun.showbalance(sdac)))
            print("You transferred " + str(transferamount)+" to "+recip.get_name())

        elif choice == 5:
            trfun.getTransaction(sdac)
        elif choice ==6:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day_1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
