# Python Banking Program

def SHOW_BALANCE(BALANCE):
    print(f"Your balance is ${BALANCE}")

def DEPOSIT():
    AMOUNT= float(input("Enter an amount to be deposited: "))

    if AMOUNT < 0:
        print("That's not a valid amount")
        return 0
    else:
        return AMOUNT
def WITHDRAW(BALANCE):
    AMOUNT = float(input("Enter amount to be withdrawn: "))

    if AMOUNT > BALANCE:
        print("Insufficient funds")
        return 0
    elif AMOUNT <= 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return AMOUNT

def main():
    BALANCE = 0
    IS_RUNNING = True

    while IS_RUNNING:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        CHOICE = input("Enter your choice (1-4): ")

        if CHOICE == '1':
            SHOW_BALANCE(BALANCE)
        elif CHOICE == '2':
            BALANCE += DEPOSIT()
        elif CHOICE == '3':
            BALANCE -= WITHDRAW(BALANCE)
        elif CHOICE == '4':
            IS_RUNNING = False
        else:
            print("That is not valid choice.")

    print("Thank you! have a nice day!")

if __name__ == '__main__':
    main()