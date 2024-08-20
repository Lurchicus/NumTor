"""
Number Torture for Python (pick a number between 1 and 100, with a twist).
"""

from random import randint
from colorama import Fore, Back


def prompt():
    """ Display prompt, error check input and re-prompt on error, return 
    numeric value if it is okay
    """
    i_got = -2
    its_good = False
    while not its_good:
        inp = input(Fore.YELLOW + " Pick a number between 1 and 100: " + Fore.WHITE)
        try:
            i_got = int(inp)
            its_good = True
        except:
            print(Back.RED + Fore.WHITE + " Invalid input (not int)!" + Fore.WHITE + Back.RESET)
    return i_got


def info(b_flag, target_val, guess_val, threshold_val, in_range_val):
    """ info(b_Flag, targetVal, guessVal, thresholdVal, in_range_val)
    If b_flag argument is True, we show debug info. """
    if b_flag:
        print(f"Target: {target_val} guess: {guess_val} "+
            f"threshold: {threshold_val} in_range: {in_range_val}")


#PROMPT = Fore.YELLOW + " Pick a number between 1 and 100: " + Fore.WHITE
print(Fore.GREEN,"Number Torture by Dan Rhea and Lee Weiss 1992-2024",Fore.WHITE)
print(Fore.GREEN,"So what's the torture? Well, along with my picking",Fore.WHITE)
print(Fore.GREEN,"a number between 1 and 100, I'll also pick a value",Fore.WHITE)
print(Fore.GREEN,"between 2 and 5. If you get near the number without",Fore.WHITE)
print(Fore.GREEN,"guessing it exactly, I'll change the number!",Fore.WHITE)
print(Fore.GREEN,"Have fun! (enter 0 to exit)",Fore.WHITE)

DEBUG = False                   # debug flag
BEST = 1000                     # best score so far
TRIES = 0                       # current number of tries
IN_RANGE = 101                   # how close the guess is to the target
GUESS = -1                      # current guess
THRESHOLD = randint(2,5)        # how close the guess has to be to the target to change it
TARGET = randint(1, 100)        # the target number

info(DEBUG, TARGET, GUESS, THRESHOLD, IN_RANGE)
GUESS = prompt()
while GUESS != 0:

    TRIES = TRIES + 1

    # Get the value of how close the guess is to the target
    if GUESS < TARGET:
        IN_RANGE = abs(TARGET-GUESS)
    else:
        IN_RANGE = abs(GUESS-TARGET)

    info(DEBUG, TARGET, GUESS, THRESHOLD, IN_RANGE)

    # Show tries and best score (if there is one)
    if GUESS != -1:
        if BEST < 1000:
            print(Back.BLUE + Fore.WHITE + " Try: " + str(TRIES) + Back.GREEN + Fore.WHITE +
                " Your best score is: " + str(BEST) + Fore.WHITE + Back.RESET)
        else:
            print(Back.BLUE + Fore.WHITE + " Try: " + str(TRIES) + Fore.WHITE + Back.RESET)

    # See if we are exiting or not
    if GUESS != 0:

        # Check for debug toggle
        if GUESS == -1:
            if DEBUG:
                DEBUG = False
            else:
                DEBUG = True
            # Decrement the try counter so the toggle doesn't count as a guess
            # and get a new guess
            TRIES = TRIES - 1
            info(DEBUG, TARGET, GUESS, THRESHOLD, IN_RANGE)
            GUESS = prompt()
            continue

        # Logic for a perfect guess
        if GUESS == TARGET:
            print(Back.GREEN + Fore.WHITE + " You got it in "+str(TRIES)+"!" +
                Fore.WHITE + Back.RESET)
            TARGET = randint(1, 100)
            THRESHOLD = randint(2,5)
            GUESS = -2
            info(DEBUG, TARGET, GUESS, THRESHOLD, IN_RANGE)

            # Adjust best score if needed
            if TRIES < BEST:
                BEST = TRIES
                TRIES = 0

        else:
            # Logic for too low
            if GUESS < TARGET:
                print(Back.RED + Fore.WHITE + " That's too low!" + Fore.WHITE + Back.RESET)

            # Logic for too high
            if GUESS > TARGET:
                print(Back.RED + Fore.WHITE + " That's too high!" + Fore.WHITE + Back.RESET)

            # Logic for a "too close" guess
            if IN_RANGE <= THRESHOLD:
                print(Back.RED + Fore.WHITE + " And "+str(GUESS)+ " is too close to "+str(TARGET)+
                    ", so I changed the number!" + Fore.WHITE + Back.RESET)
                TARGET = randint(1, 100)
                THRESHOLD = randint(2,5)
                info(DEBUG, TARGET, GUESS, THRESHOLD, IN_RANGE)

        # Get the next guess
        GUESS = prompt()

# Later
print(Back.GREEN + Fore.WHITE," Goodbye!",Fore.WHITE + Back.RESET)
