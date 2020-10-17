"""
File: hangman_謝濡駿.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7
# This constant allows the game to be extended to use the words with more characters.
N_GUESSES = 100


def main():
    """
    crucial point is using string substitution technique to piece the answer together
    """
    w = random_word()
    ans = '-' * len(w)  # Let ans as a word filled with blank.
    print('The word looks like: ' + ans)
    print('You have ' + str(N_TURNS) + ' guesses left.')
    n = N_TURNS
    for i in range(N_GUESSES):  # Allows longer word to be guessed.
        a = input('Your guess: ')
        ua = a.upper()  # check case-insensitive
        if w.find(ua) == -1:
            print('There is no ' + ua + 's in the word.')
            n -= 1
            if n == 0:
                print('You are completely hung :(')
                print('The word was: ' + w)
                break
            else:
                print('You have ' + str(n) + ' guesses left.')
        else:
            for j in range(len(w)):
                ch = w[j]
                if ua == ch:
                    ans = ans[0:j] + ch + ans[j+1:]
                else:
                    ans = ans[0:j] + ans[j] + ans[j+1:]
            print('You are correct!')
        if ans == w:  # check if the game still on
            print('You win!!')
            print('The word was: ' + w)
            break
        else:
            print('The word looks like: ' + ans)


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
