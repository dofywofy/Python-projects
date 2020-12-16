import random
print("Hello, what is your name?")
name=input()
print("Nice to meet you",name,"Let us being our guessing game?")
print("You have to think of a number between 1 to 20 and you have to guess it in less than 6 guesses.")
number = random.randint(1,20)
guess_no = 0
while (guess_no < 6) :
    print("Take a guess :")
    guess = input()
    guess = int(guess)
    guess_no = guess_no + 1
    if (guess < number) :
        print("Wrong, your guess is lower than the number.")
    if (guess > number) :
        print("Wrong, your guess is higher than the number.")
    if (guess == number) :
        break;
if (guess == number) :
    print("You won! Great job",name,"! You guessed the number in",guess_no,"guesses!")
if (guess != number) :
    print("Sorry, You ran out of guesses! The number was",number)
    print("Better luck next time.")
