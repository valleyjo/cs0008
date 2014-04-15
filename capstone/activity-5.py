#Email: amv49@pitt.edu
#Name: Alex Vallejo
#ID: 3578411
#Date: 2/19/2014
#Description: This program is the game of craps!

import random

class Dice:

  def roll(): # Roll the dicendom
    return random.randint(1,6);

def welcome():
  user_name = input("Enter your name: "); #Get the user's name
  print("\nWelcome " + user_name + "!");  #Print a nice welcome message
  print("This game of craps was written by Alex Vallejo <amv49@pitt.edu>\n") #Tell 'em who write this!
  print("Instructions:"); #Display the instructions!
  print("A new shooter (player) begins his roll. This is known as the come out " +
        "roll. If the shooter rolls a 7 or 11 you win. If the shooter rolls a 2, " +
        "3 or 12, you lose. If the shooter rolls any other number, that number " +
        "becomes the point number. The shooter must roll that number again before " +
        "a seven is rolled. If that happens, you win. If a seven is rolled before " +
        "the point number is rolled again, you lose. ");
  return user_name;

user_name = welcome()
num_times = 0;
times_played = int(input("Enter the number of times the game should be played: "));

while (num_times <= times_played):
  game_over = False;  # Boolean flag used to keep the game running

  shooter_roll = Dice.roll() + Dice.roll()
  print("\nShooter rolls: ", shooter_roll);

  # Player wins if the computer rolls 7 or 11
  if (shooter_roll == 7 or shooter_roll == 11):
    game_over = True;
    print("Congrats, you win!");

  # Computer wins if it rolls 2, 3 or 12
  elif (shooter_roll == 2 or shooter_roll == 3 or shooter_roll == 12):
    game_over = True;
    print("Sorry, you lose!");

  # The point number becomes the roll
  else:
    point_number = shooter_roll;
    print("The point number is: ", point_number);

  # While the game is not over, keep rollin'
  while (not game_over):
    roll = random.randint(1,12)

    print("Roll: ", roll);

    # If the computer rolls the point number, player wins!
    if (roll == point_number):
      game_over = True;
      print("Congrats, you win!");

    # If the computer rolls 7, the computer wins!
    if (roll == 7):
      game_over = True;
      print("Sorry, you lose!");

  num_times += 1;

# Print a nice message to thank the user for playing
print("Thanks for playing", user_name,"!");

