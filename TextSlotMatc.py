balance = 0

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
    balance += deposit()
    print("Your balance is:", balance)

main()