from random import randint
from colorama import Fore, Back

prompt = Fore.YELLOW + " Pick a bumber between 1 and 100: " + Fore.WHITE
print(Fore.GREEN,"Number Torture by Dan Rhea and Lee Weiss 1992-2024",Fore.WHITE)
print(Fore.GREEN,"So what's the torture? Well, along with my picking",Fore.WHITE)
print(Fore.GREEN,"a number between 1 and 100, I'll also pick a value",Fore.WHITE)
print(Fore.GREEN,"between 2 and 5. If you get near the number without",Fore.WHITE)
print(Fore.GREEN,"guessing it exactly, I'll change the number!",Fore.WHITE)
print(Fore.GREEN,"Have fun! (enter 0 to exit)",Fore.WHITE)

best = 1000                     # best score so far
tries = 0                       # current number of tries
inrange = 101                   # how close the guess is to the target
guess = -1                      # current guess
threshold = randint(2,5)        # how close the guess has to be to the target to change it
target = randint(1, 100)        # the target number
#debug = "Target: " + str(target) + " guess: " + str(guess) + " threshold: " + str(threshold) + " inrange: " + str(inrange)
#print(debug)
guess = int(input(prompt))
while guess != 0:

        tries = tries + 1

        # Get the value of how close the guess is to the target
        if guess < target:
                inrange = abs(target-guess)
        else:
                inrange = abs(guess-target)

        #debug = "Target: " + str(target) + " guess: " + str(guess) + " threshold: " + str(threshold) + " inrange: " + str(inrange)
        #print(debug)

        # Show tries and best score (if there is one)
        if best < 1000:
                print(Back.BLUE + Fore.BLACK + " Try: " + str(tries) + Back.GREEN + Fore.BLACK + " Your best score is: " + str(best) + Fore.WHITE + Back.RESET)
        else:
                print(Back.BLUE + Fore.BLACK + " Try: " + str(tries) + Fore.WHITE + Back.RESET)

        # See if we are exiting or not
        if guess != 0:

                # Logic for a perfect guess
                if guess == target:
                        print(Back.GREEN + Fore.BLACK + " You got it in "+str(tries)+"!" + Fore.WHITE + Back.RESET)
                        target = randint(1, 100)
                        threshold = randint(2,5)
                        guess = -1
                        #debug = "Target: " + str(target) + " guess: " + str(guess) + " threshold: " + str(threshold) + " inrange: " + str(inrange)
                        #print(debug)
                        if tries < best:
                                best = tries
                        tries = 0
                else:
                        # Logic for too low
                        if guess < target:
                                print(Back.RED + Fore.BLACK + " That's too low!" + Fore.WHITE + Back.RESET)
                        
                        # Logic for too high
                        if guess > target:
                                print(Back.RED + Fore.BLACK + " That's too high!" + Fore.WHITE + Back.RESET)

                        # Logic for a "too close" guess
                        if inrange <= threshold:
                                print(Back.RED + Fore.BLACK + " And "+str(guess)+ " is too close to "+str(target)+", so I changed the number!" + Fore.WHITE + Back.RESET)
                                target = randint(1, 100)
                                threshold = randint(2,5)
                                #debug = "Target: " + str(target) + " guess: " + str(guess) + " threshold: " + str(threshold) + " inrange: " + str(inrange)
                                #print(debug)

        # Get the next guess
        guess = int(input(prompt))

# Later 
print(Back.GREEN + Fore.BLACK," Goodbye!",Fore.WHITE + Back.RESET)

        
                          