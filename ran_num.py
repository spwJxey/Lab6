import random

def is_num(value):
  """
  Checks if number is greater than 0 and returns the absolute value of negative integers
  """
  if value < 0:
    print("Your number has been rounded to the abosolute value")
    return -value
  elif value == 0:
    print(str(value) + " is an invalid input, please enter a number greater than 0 ")
    play_game()
  else:
    return value
    
def guess(random, range):
  guess_input = int(input("Please guess a possitive integer between 0 and " + str(range) + ": ")) 
  if guess_input > random:
    print("Your guess is high")
    guess(random, range)
  elif guess_input < random:
    print("Your guess is low")
    guess(random, range)
  else:
    print("You are correct! " + str(random) + " is the random number")
    restart = input("Would you like to play again? (Please enter Yes or No): ")
    
    if (restart == "Yes" or restart == "Y" or restart == "yes" or restart == "YES" or restart == "yes"):
        play_game()
    else:
      print("Have a good day!")

def play_game():
  max = int(input("Pick a possitive integer: "))
  max = is_num(max)
    
  random_number = random.randint(0, max)
  guess(random_number, max)

play_game()