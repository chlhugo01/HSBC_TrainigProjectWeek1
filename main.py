import account as ac
import transaction as tr
import transfunctions as trfun
import customer as ct

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def day_1():
    cuslist = [{"id": 1, "name": "Hugo",'email':"hugo@gmail.com",'address':'hsbc' },
               {"id": 2, "name": "Cora", 'email':"Cora@gmail.com",'address':'hsbc'},
               {"id": 3, "name": "John", 'email':"John@gmail.com",'address':'hsbc'},
               {"id": 4, "name": "Alvin", 'email':"Alvin@gmail.com",'address':'hsbc'},
               {"id": 5, "name": "Bell",'email':"Bell@gmail.com",'address':'hsbc' }
               ]
    cclasslist = []

    for i in range(0,len(cuslist)):
        temp = ct.customer(i+1 , cuslist[i]["name"],cuslist[i]['email'],cuslist[i]['address'])
        temp.accountList.append(ac.account(i+1,0))   # account id same as customer id
        cclasslist.append(temp)

    cus = input('Please enter your customer name:')
    for i in range(len(cclasslist)):
        if(cclasslist[i].name == cus):
            cus = cclasslist[i]
            break;
        else:
            print("no customer found")
            exit()
    
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

            for i in range(len(cclasslist)):
                if (cclasslist[i].name == recip):
                    recip = cclasslist[i]
                    break;

            trfun.transfer(transferamount,cus.accountList[0],recip.accountList[0])
            
            print("Your balance:  " + str(trfun.showbalance(cus.accountList[0])))
            print("You transferred " + str(transferamount)+" to "+recip.name)

        elif choice == 5:
            trfun.getTransaction(cus.accountList[0])
        elif choice ==6:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    day_1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
