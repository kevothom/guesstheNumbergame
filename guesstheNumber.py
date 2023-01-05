# This is a guess the number game.
import random # program imports the random module which enables program to use random.randint() function
secretNumber = random.randint(1, 50) # variable secretNumber declared for return value
print("I am thinking of a number between 1 and 50") # print statement asking player to input/guess number from 1 to 50

#Ask the player to guess 8 times.
for guessesTaken in range(1, 9): # for loop using range function, loops up to 8 times
    print("Take a guess.") # print statement prompting user to take a guess
    guess = int(input()) 
    
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break # This condition is the correcgt guess!
    
if guess ==secretNumber:
    print("Great job! You have guessed the Secret Number in " + str(guessesTaken) + ' guesses!')
else:
    print("Nope. Please try again,the Number I was thinking of was " + str(secretNumber))    