import random
number = random.randint(1, 10)
no_of_guesses = 0
name =  input("Hi! What's your name? ")
print("Okay!" + name + "I'm guessing a number between 1-10" )
while no_of_guesses < 5:
    guess = int(input()) 
    no_of_guesses += 1
    if(guess > number):
        print("Your guess is high")
    if(guess < number):
        print("Your guess is low")
    if(guess == number):
        break
if guess == number:
    print("You guessed the right number in " + str(no_of_guesses) + "tries")
else:
    print("Sorry your guess as worng")