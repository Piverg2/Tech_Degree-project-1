# Python Web Development Techdegree
# Project 1 - Number Guessing Game - Gavyn Piver
# --------------------------------
import random


def start_game():
    print("  -------------------------------  ")
    print("Welcome to the Number Guessing Game!")
    print("  -------------------------------  ")
    guess = int(input("Pick a number between 1 and 10: "))
    tries = 1
    # Had to look up how to use Random and randomint. Source: https://www.w3schools.com/python/ref_random_randint.asp
    answer = random.randint(1, 10)
    if guess == answer:
      print("Awesome! you guessed the answer on the first!")
    while guess != answer:
      tries += 1
      if guess > answer:
        print("It's lower")
      if guess < answer:
        print("It's higher")
      guess = int(input("Try Again! Pick a number between 1 and 10: "))
      if guess == answer:
        print("\nYou did it! It took you {} tries to guess the number".format(tries))
        print("-------------- ")
        print("  Game Over!")
        print("-------------- ")
        break
    play_again = input("Would you like to playe again? (Y/N) ")
    if play_again.lower() == "y":
      start_game()
    else:
      print("Thanks for playing!")
start_game()
