#Email: amv49@pitt.edu
#Name: Alex Vallejo
#ID: 3578411
#Date: 2/19/2014
#Description: This program is the game of craps!

import random

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
