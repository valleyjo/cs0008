#Email: amv49@pitt.edu
#Name: Alex Vallejo
#ID: 3578411
#Date: 2/19/2014
#Description: This program is the game of craps!

import random

user_name = input("Enter your name: ");
print("\nWelcome " + user_name + "!");
print("This game of craps was written by Alex Vallejo <amv49@pitt.edu>\n");
print("Instructions:");
print("A new shooter (player) begins his roll. This is known as the come out " +
      "roll. If the shooter rolls a 7 or 11 you win. If the shooter rolls a 2, " +
      "3 or 12, you lose. If the shooter rolls any other number, that number " +
      "becomes the point number. The shooter must roll that number again before " +
      "a seven is rolled. If that happens, you win. If a seven is rolled before " +
      "the point number is rolled again, you lose. ");

game_over = False;

shooter_roll = random.randint(1,12);
print("\nShooter rolls: ", shooter_roll);

if (shooter_roll == 7 or shooter_roll == 11):
  game_over = True;
  print("Congrats, you win!");

elif (shooter_roll == 2 or shooter_roll == 3 or shooter_roll == 12):
  game_over = True;
  print("Sorry, you lose!");

else:
  point_number = shooter_roll;
  print("The point number is: ", point_number);

while (not game_over):
  roll = random.randint(1,12)

  print("Roll: ", roll);

  if (roll == point_number):
    game_over = True;
    print("Congrats, you win!");

  if (roll == 7):
    game_over = True;
    print("Sorry, you lose!");

print("Thanks for playing", user_name,"!");

