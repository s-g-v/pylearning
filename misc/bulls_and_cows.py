#!/usr/bin/env python3

import random
import sys

def _come_up_number():
    return str(random.randint(1000,9999))


def _match_input(pc_number, user_number):
    bulls=0
    cows=0
    for i, digit in enumerate(user_number):
        if digit in pc_number:
            bulls+=1
        if user_number[i] == pc_number[i]:
            cows+=1
    return (bulls, cows)


def _user_input():
    user_number = input()
    while not (len(user_number) == 4 and user_number.isdigit()):
        if user_number.lower() in ("exit","quit","q"):
            print("Good buy!")
            sys.exit()
        print("Please enter four-digit number, or 'exit', 'quit', 'q' to finish game")
        user_number = input()
    return user_number


def play():
    """-=Bulls and cows game=-
PC comes up four-digit number. Try to quess it.
After each step you will see response:
    First digit - how much digits from your variant is in PC's number.
    Second digit - how much of them is on the place.
Good luck!"""
    print(play.__doc__)
    pc_number = _come_up_number()
    print("Please enter four-digit number, or 'exit', 'quit', 'q' to finish game")
    result = ()
    while result != (4, 4):
        user_number = _user_input()
        result = _match_input(pc_number, user_number)
        print(str(result))
    print("You are win!")


if __name__ == "__main__":
    play()