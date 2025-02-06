## Name: Cory Strong
## Class: CSCI 101
## File Name : LuckySevens_CStrong.py
## Description : This code is a game that tells the users how much rolls it takes to lose all of their money that they
# input, showing that the game is not profitable.

Header = "Lucky Sevens"
print('-'*30)
print('-'*30)
print('-' + Header.center(28) + '-')
print('-'*30)
print('-'*30)
print("")
print("")

import random
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def lucky_sevens(initial_funds):
    funds = initial_funds
    rolls = 0
    max_funds = funds
    max_roll = 0

    while funds > 0:
        rolls += 1
        dice_sum = roll_dice()

        if dice_sum == 7:
            funds += 4
        else:
            funds -= 1

        if funds > max_funds:
            max_funds = funds
            max_roll = rolls

    return rolls, max_funds, max_roll

def main():
    try:
        initial_funds = int(input("Please enter the amount of money you'd like to start with (whole numbers only): "))
        if initial_funds <= 0:
            print("Please enter a positive amount of money.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
        return

    rolls, max_funds, max_roll = lucky_sevens(initial_funds)

    print(f"You are broke after {rolls} rolls.")
    print(f"You should have quite after {max_roll} rolls, when you had ${max_funds}.")

if __name__ == "__main__":
    main()



