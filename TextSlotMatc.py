balance = 0

def get_menu(balance):
        menu_text = f"""----- SLOT MACHINE -----
        Balance: €{balance}
        1 - Deposit
        2 - Play
        3 - Withdraw
        4 - Exit"""

        print(menu_text)
        choice = int(input("What do you want to do"))
        return choice


    

def deposit():
        while True:
            try:
                amount = int(input("How much would you like to deposit? "))

                if amount <= 0:
                    print("You must deposit a number greater than 0")
                else:
                        return amount

            except ValueError:
                    print("Invalid input. Please enter a number")





def main():
    global balance
    while True:
        choice = get_menu(balance)

        if choice == "1":
              balance += deposit()
              print("You balance is:", balance)

main()