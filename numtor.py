"""
Number Torture for Python (pick a number between 1 and 100, with a twist).
"""

import random
from colorama import Fore, Back


def prompt() -> int:
    """ 
    Display prompt, error check input and re-prompt on error, return 
    numeric value if it is okay
    """
    i_got = -2
    its_good = False
    while not its_good:
        inp = input(f"{Fore.YELLOW} Pick a number between 1 and 100 (or 0 to exit): {Fore.WHITE}")
        try:
            i_got = int(inp)
            its_good = True
        except ValueError:
            print(f"{Back.RED}{Fore.WHITE} Invalid input (not an integer)!{Fore.WHITE}{Back.RESET}")
    return i_got


def info(b_flag, target_val, guess_val, threshold_val, in_range_val) -> None:
    """ 
    info(b_Flag, targetVal, guessVal, thresholdVal, in_range_val)
    If b_flag argument is True, we show debug info. 
    """
    if b_flag:
        print(f"Target: {target_val} guess: {guess_val} "+
            f"threshold: {threshold_val} in_range: {in_range_val}")


def main() -> None:
    """ 
    Main function to run the game. 
    """
    print(f"{Fore.GREEN}Number Torture by Dan Rhea and Lee Weiss 1991-2024")
    print("So what's the torture? Well, along with my picking")
    print("a number between 1 and 100, I'll also pick a value")
    print("between 2 and 5. If you get near the number without")
    print("guessing it exactly, I'll change the number!")
    print(f"Have fun! (enter 0 to exit){Fore.WHITE}")

    debug: bool = False             # debug flag
    best: int = 1000                # best score so far
    tries: int = 0                  # current number of tries
    in_range: int = 101             # how close the guess is to the target
    guess: int = -1                 # current guess
    threshold: int = random.randint(2,5)   # how close the guess has to be to the target to change it
    target: int = random.randint(1, 100)   # the target number

    info(debug, target, guess, threshold, in_range)
    guess = prompt()
    while guess != 0:

        tries += 1

        # Get the value of how close the guess is to the target
        if guess < target:
            in_range = abs(target-guess)
        else:
            in_range = abs(guess-target)

        info(debug, target, guess, threshold, in_range)

        # Show tries and best score (if there is one)
        if guess != -1:
            if best < 1000:
                print(f"{Back.BLUE}{Fore.WHITE} Try: {str(tries)}{Back.GREEN}{Fore.WHITE}"
                    f" Your best score is: {str(best)}{Fore.WHITE}{Back.RESET}")
            else:
                print(f"{Back.BLUE}{Fore.WHITE} Try: {str(tries)}{Fore.WHITE}{Back.RESET}")

        # See if we are exiting or not
        if guess != 0:

            # Check for debug toggle
            if guess == -1:
                if debug:
                    debug = False
                else:
                    debug = True
                # Decrement the try counter so the toggle doesn't count as a guess
                # and get a new guess
                tries -= 1
                info(debug, target, guess, threshold, in_range)
                guess = prompt()
                continue

            # Logic for a perfect guess
            if guess == target:
                print(f"{Back.GREEN}{Fore.WHITE} You got it in {str(tries)}!"
                    f"{Fore.WHITE}{Back.RESET}")
                target = random.randint(1, 100)
                threshold = random.randint(2,5)
                guess = -2
                info(debug, target, guess, threshold, in_range)

                # Adjust best score if needed
                if tries < best:
                    best = tries
                    tries = 0

            else:
                # Logic for too low
                if guess < target:
                    print(f"{Back.RED}{Fore.WHITE} That's too low!{Fore.WHITE}{Back.RESET}")

                # Logic for too high
                if guess > target:
                    print(f"{Back.RED}{Fore.WHITE} That's too high!{Fore.WHITE}{Back.RESET}")

                # Logic for a "too close" guess
                if in_range <= threshold:
                    print(f"{Back.RED}{Fore.WHITE} And {str(guess)} is too close to {str(target)}"
                        f", so I changed the number!{Fore.WHITE}{Back.RESET}")
                    target = random.randint(1, 100)
                    threshold = random.randint(2,5)
                    info(debug, target, guess, threshold, in_range)

            # Get the next guess
            guess = prompt()

    # Later
    print(f"{Back.GREEN}{Fore.WHITE} Goodbye!{Fore.RESET}{Back.RESET}")


if __name__ == "__main__":
    main()
