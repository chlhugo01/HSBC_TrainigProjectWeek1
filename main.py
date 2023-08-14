import account as ac
import transaction as tr
import transfunctions as trfun
import customer as ct

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def day_1():
    """""
    cuslist = [{"id":1,"name":"Hugo","balance":0},
               {"id":2,"name":"Cora","balance":0},
               {"id":3,"name":"John","balance":0},
               {"id":4,"name":"Alvin","balance":0},
               {"id":5,"name":"Bell","balance":0}
            ]
    
    cclasslist=[]
    
    for i in range(len(cuslist)):
        temp = customer.customer(cus[i]["id"],cus[i]["name"],cus[i]["balance"])
        cclasslist.append(temp)
    
    """
    cus1 = ct.customer(1,"Hugo","test@gmail.com","hsbc")
    cus1.accountList.append(ac.account(1,0))
    cus2 = ct.customer(2, "Cora", "test@gmail.com","hsbc")
    cus2.accountList.append(ac.account(2,0))
    cus3 = ct.customer(3, "John", "test@gmail.com","hsbc")
    cus3.accountList.append(ac.account(3,0))
    cus4 = ct.customer(4, "Alvin", "test@gmail.com","hsbc")
    cus4.accountList.append(ac.account(4,0))
    cus5 = ct.customer(5, "Bell", "test@gmail.com","hsbc")
    cus5.accountList.append(ac.account(5,0))
    #cus5.accountList.append(6)
    
    
    cus = input('Please enter your customer ID:')
    
    """""
    for i in range(len(cclasslist)):
            temp = customer.customer(cus[i]["id"],cus[i]["name"],cus[i]["balance"])
            cclasslist.append(temp)
    
    """""
    
    if cus == "cus1":
        cus = cus1
    elif cus == "cus2":
        cus = cus2
    elif cus == "cus3":
        cus = cus3
    elif cus == "cus4":
        cus = cus4
    elif cus == "cus5":
        cus = cus5
    
    
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
            print(trfun.showbalance(cus.accountList[0]))
            print("Your balance:  " + str(trfun.showbalance(cus.accountList[0])))
        elif choice == 2:
            withdrawamount = int(input("How much you want to withdraw"))
            if trfun.withdraw(withdrawamount,cus.accountList[0]):
                print("Your balance:  " + str(trfun.showbalance(cus.accountList[0])))
                print("You withdraw" + str(withdrawamount))
            else:
                print("Your withdrawal is not approved, not enough balance")
        elif choice == 3:
            
            depositamount = int(input("How much you want to deposit"))
            trfun.deposit(depositamount,cus.accountList[0])
            print("Your balance:  " + str(trfun.showbalance(cus.accountList[0])))
            print("You withdraw" + str(depositamount))
            
        elif choice==4:
            transferamount = int(input("How much you want to transfer"))
            recip=input("Who do you want to transfer to?")
            if recip == "cus1":
                recip = cus1
            elif recip == "cus2":
                    recip = cus2
            elif recip == "cus3":
                    recip = cus3
            elif recip == "cus4":
                    recip = cus4
            elif recip == "cus5":
                    recip = cus5
            trfun.transfer(transferamount,cus.accountList[0],recip.accountList[0])
            
            print("Your balance:  " + str(trfun.showbalance(cus.accountList[0])))
            print("You transferred " + str(transferamount)+" to "+recip.name)
            
        elif choice == 5:
            trfun.getTransaction(cus.accountList[0])
        elif choice ==6:
            break

    """
    customer A 500 to customer B
    A.transfer( -500 ,B)
    B.transfer(B, +500)
    """

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day_1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
