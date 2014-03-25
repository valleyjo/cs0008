#Author: Alex Vallejo <amv49@pitt.edu>
#ID: 3578411
#Description: This program is a simple game of hangman.

import sys

def game_over(word):
    print("\nYou lose but thanks for playing.")
    print("The word was \"" + word + "\"")
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

def user_input():
    user_guess = input("\nGuess a letter: ")
    while (len(user_guess) != 1 or not user_guess.isalpha()):

        if (not user_guess.isalpha()):
            print("You must enter a letter as a guess. Try again.")
        elif (len(user_guess) > 1):
            print("You can only enter a 1 letter guess. Try again.")

        user_guess = input("Guess a letter: ")

    return user_guess.lower()

def main():
    word = list("balls")
    guess = list("")
    wrong_guesses = 0;
    letters = {}

    for num in range(97,123): # init dictionary to ASCII values from a-z
        letters[num] = False

    for letter in word:
        guess += "_"

    while "_" in guess:
        print("\nYour guess so far: " + "".join(guess))
        user_guess = user_input()
        if user_guess in word:
            print("Good guess! The letter '" + user_guess + "' is in the word")
            for i, letter in enumerate(word):
                if letter == user_guess:
                    guess[i] = user_guess
        else:
            wrong_guesses += 1
            print("Sorry, the letter '" + user_guess + "' is not in the word.")
            print_man(wrong_guesses)

        if wrong_guesses == 6:
            game_over("".join(word))

    print("\nCongrats! You win. The word was " + "".join(word))

main()

