# Python Web Development Techdegree
# Project 1 - Number Guessing Game - Gavyn Piver
# --------------------------------
import random


def start_game():

  def guess_number():
    try:
      guess = int(input("Pick a number between 1 and 10: "))
    except ValueError:
      guess = int(
          input("Sorry! That is not a number. Pick a number between 1 and 10: "))
    return guess

  print("  -------------------------------  ")
  print("Welcome to the Number Guessing Game!")
  print("  -------------------------------  ")
  guess = guess_number()
  tries = 1
  # Had to look up how to use Random and randomint. Source: https://www.w3schools.com/python/ref_random_randint.asp
  answer = random.randint(1, 10)

  while guess != answer:
    tries += 1
    try:
      if guess > 10:
        print("\nThat number is not between 1 and 10!")
        guess = guess_number()
        continue
      elif guess > answer:
        print("\nIt's lower")
        guess = guess_number()
        continue
      elif guess < answer:
        print("\nIt's higher")
        guess = guess_number()
        continue
      else:
        break
    except ValueError:
      guess = int(
          input("Sorry! That is not a number. Pick a number between 1 and 10: "))
  if guess == answer:
    if tries == 1:
      print("Awesome! You guessed the answer on the first try!")
    else:
      print("\nAwesome! You guessed the answer in {} tries!".format(tries))
    play_again = input("Would you like to play again? (Y/N) ")
    if play_again.lower() == "y":
      start_game()
    else:
      print("\nThanks for playing!")


start_game()
