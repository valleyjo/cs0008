#Author: Alex Vallejo <amv49@pitt.edu>
#ID: 3578411
#Description: This program is a simple game of hangman.

import sys, random

class Word():
    word = {}
    hint = ""

    def __init__(self, word, hint):
        self.word = list(word)
        self.hint = hint

def game_over(word):
    sys.exit(0)

def print_man(wrong_guesses):

    if (wrong_guesses > 6 or wrong_guesses < 0):
        print("ERROR in print_man(int)")
        print("System exiting...")
        sys.exit(1)

    print("\n-----|")

    if wrong_guesses == 1:
        print("   ('_')")
    elif wrong_guesses == 2:
        print("   ('_')")
        print("     |")
    elif wrong_guesses == 3:
        print("   ('_')")
        print("    -|")
    elif wrong_guesses == 4:
        print("   ('_')")
        print("    -|-")
    elif wrong_guesses == 5:
        print("   ('_')")
        print("    -|-")
        print("    /")
    elif wrong_guesses == 6:
        print("   ('_')")
        print("    -|-")
        print("    / \\")

def user_input(letters):
    user_guess = input("\nGuess a letter: ")
    while ( len(user_guess) != 1
            or not user_guess.isalpha()
            or user_guess in letters):

        if (not user_guess.isalpha()):
            print("You must enter a letter as a guess. Try again.")
        elif (len(user_guess) > 1):
            print("You can only enter a 1 letter guess. Try again.")
        elif (user_guess in letters):
            print("You already guessed '" + user_guess + "' before.")

        user_guess = input("Guess a letter: ")

    return user_guess.lower()

def main():

    games_played = 0

    # Read the file and store the words
    words = list()
    f = open("hint_dict.txt")
    for line in f:
        values = line.split(",")
        words.append(Word(values.pop(0), values.pop(0)))

    random.shuffle(words)

    # While the list has words in it keep playing
    while True:

      games_played += 1
      if games_played > 3:
        again = input("Do you want to continue playing? (y/n): ")
        if (again == "n"):
            sys.exit(0)

      if not words:
        print("\nNo words left! Game over!")
        sys.exit(0)

      guess = list("")
      wrong_guesses = 0;
      guessed_letters = list()
      word = words.pop()

      for letter in word.word:
          guess += "_"

      while "_" in guess:

          if (not guessed_letters):
              print("\nThe next word has " + str(len(word.word)) + " letters.")
              print("The hint is:" + word.hint)
          else:
              print("\nYour guess so far: " + "".join(guess))

          user_guess = user_input(guessed_letters)
          guessed_letters.append(user_guess)

          if user_guess in word.word:
            print("Good guess! The letter '" + user_guess + "' is in the word")
            for i, letter in enumerate(word.word):
                if letter == user_guess:
                    guess[i] = user_guess
          else:
              wrong_guesses += 1
              print("Sorry, the letter '" + user_guess + "' is not in the word.")
              print_man(wrong_guesses)

          if wrong_guesses == 6:
              print("\nYou lose but thanks for playing.")
              print("The word was \"" + "".join(word.word) + "\"")
              break
      if "_" not in guess:
        print("\nCongrats! You win. The word was \"" + "".join(word.word) + "\"")

main()

