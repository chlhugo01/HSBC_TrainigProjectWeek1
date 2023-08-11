import customer
import transaction


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def day_1():
    cus1 = customer.customer(1,"Hugo",0)
    cus2 = customer.customer(2, "Cora", 0)
    cus3 = customer.customer(3, "John", 0)
    cus4 = customer.customer(4, "Alvin", 0)
    cus5 = customer.customer(5, "Bell", 0)
    while 1:
        cus = input('Which customer are you?')
        if customer == "cus1":
            cus = cus1
        elif customer == "cus2":
            cus = cus2
        elif customer == "cus3":
            cus = cus3
        elif customer == "cus4":
            cus = cus4
        elif customer == "cus5":
            cus = cus5

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
            print("Your balance:  " + str(cus.showbalance()))
        elif choice == 2:
            withdrawamount = int(input("How much you want to withdraw"))
            if cus.withdraw(withdrawamount):
                print("Your balance:  " + str(cus.showbalance()))
                print("You withdraw" + str(withdrawamount))
            else:
                print("Your withdrawal is not approved, not enough balance")
        elif choice == 3:
            depositamount = int(input("How much you want to deposit"))
            cus.deposit(depositamount)
            print("Your balance:  " + str(cus.showbalance()))
            print("You withdraw" + str(depositamount))


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
