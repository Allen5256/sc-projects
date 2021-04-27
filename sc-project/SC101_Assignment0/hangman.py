"""
File: hangman.py
Name: Allen Lee
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    Firstly, a variable guess_left is assigned to calculate how many guesses left users have,
    and a variable dashed is assigned to be a string including only '-'.
    Next, a while loop is used to ensure users can make guesses infinitely (if users do not make wrong guesses).
    And then, several if and elif statement is used to separate different situations.
    1. input_ch is not an alphabet:
        print('illegal format')
    2. input_ch is not in the answer:
        guess_left minuses 1.
        (while guess_left reaches 0, the while loop will break and show the failure result.)
    3. input_ch is in the answer:
        assign new_dashed to store a new string including the alphabet users guess correctly,
        and reassign dashed to be new_dashed to ensure dashed can be updated when the while loop restarts.
        (while dashed equals to the answer, the while loop will break and show the success result.)
    """
    ans = random_word()
    guess_left = N_TURNS
    dashed = ''
    for i in range(len(ans)):
        dashed += '-'
    print('The word looks like: '+dashed)
    while True:
        print('You have '+str(guess_left)+' guesses left')
        input_ch = input('Your guess: ')
        input_ch = input_ch.upper()
        if not input_ch.isalpha:
            print('illegal format.')
        elif input_ch not in ans:
            guess_left -= 1
            if guess_left == 0:
                break
            print('There is no '+input_ch+'\'s in the word.\nThe word looks like: '+dashed)
        elif input_ch in ans:
            new_dashed = ''
            for i in range(len(ans)):
                if ans[i] == input_ch:
                    new_dashed += input_ch
                else:
                    new_dashed += dashed[i]
            if new_dashed == ans:
                break
            dashed = new_dashed
            print('You are correct!\nThe word looks like: '+dashed)
    if guess_left == 0:
        print('You are completely hung : (\nThe word was: '+ans)
    else:
        print('You win!!\nThe word was: '+ans)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
