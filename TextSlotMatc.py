import random
MIN_LINES = 1
MAX_LINES = 3

ROWS = 3
COLS = 3
def get_menu(balance):
    menu_text = f"""----- SLOT MACHINE -----
Balance: €{balance}
1 - Deposit
2 - Play
3 - Withdraw
4 - Exit
"""
    print(menu_text)
    choice = input("What do you want to do: ")
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


def withdraw(balance):
    print(f"Your balance is: {balance}")
    while True:
        try:
            amount = int(input("How much would you like to withdraw? "))

            if amount <= 0 or amount > balance:
                print("Enter a number greater than 0 and less than your balance")
            else:
                return amount

        except ValueError:
            print("Invalid input. Please enter a number")


SYMBOLS = ["🍒","🍋","🔔","⭐","💎","7"]

def get_bet():
    while True:

        try:
            bet = int(input("How much do you want to bet per line??"))
            if bet <= 0:
                print("Bet must be greater than 0")
            else:
                return bet


        except ValueError:
            print("Invalid input please enter a number")



def spin():

    grid = []
    for row in range(ROWS):
        current_row = []

        for col in range(COLS):
            symbols = random.choice(SYMBOLS)
            current_row.append(symbols)

        grid.append(current_row)

    return grid




def check_win(grid, bet, lines):
    winnings = 0

    for line in range(lines):
        symbol = grid[line][0]

        for col in range(1, COLS):
            if grid[line][col] != symbol:
                break
        else:
            winnings += bet * 5

    return winnings
    






def bet_lines():
    while True:
        
        try:
            lines = int(input(f"How many lines do you want to bet on ({MIN_LINES}-{MAX_LINES})? "))
            if lines > MAX_LINES or lines < MIN_LINES:
                print(f"Enter a number between {MIN_LINES} - {MAX_LINES}")


            else:
                return lines
        except ValueError:
            print("Invalid input. please enter a number")
    


def main():
    balance = 0
    
    while True:
        choice = get_menu(balance)

        if choice == "1":
            print("Deposit ---")
            balance += deposit()
            print("Your balance is:", balance)

        elif choice == "2":
            print("Game starts here")

            lines = bet_lines()
            bet = get_bet()

            total_bet = lines * bet
            print(f"Total bet = {total_bet}")

            if total_bet > balance:
                print("You don't have enough money!")
                continue

            grid = spin()

            grid = spin()

            print("\nSpinning...\n")
            for row in grid:
                print(" | ".join(row))

            winnings = check_win(grid, bet, lines)

            if winnings > 0:
                print(f"You won €{winnings}!")
            else:
                print("You lost!")

            balance += winnings - total_bet

            print(f"New balance: €{balance}")

        elif choice == "3":
            print("Withdraw ---")
            balance -= withdraw(balance)
            print(f"Your balance is: {balance}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")


main()