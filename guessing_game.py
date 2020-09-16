# Python Web Development Techdegree
# Project 1 - Number Guessing Game - Gavyn Piver
# --------------------------------
import random


def start_game():
  answer = random.randint(1, 10)

  def guess_number():
    while True:
      try:
        guess = input("Pick a number between 1 and 10: ")
        guess = int(guess)
        break
      except ValueError:
        print("\nSorry! That is not a number.. Please try again..")
    return guess

  print("  -------------------------------  ")
  print("Welcome to the Number Guessing Game!")
  print("  -------------------------------  ")
  tries = 1
  guess = guess_number()
  # Had to look up how to use Random and randomint. Source: https://www.w3schools.com/python/ref_random_randint.asp

  
  while guess != answer:
    tries += 1
    if guess > 10:
      print("\nThat number is not between 1 and 10!")
      guess = guess_number()
    elif guess > answer:
      print("\nIt's lower")
      guess = guess_number()
    elif guess < answer:
      print("\nIt's higher")
      guess = guess_number()
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
