#Game guess the number
import random
print("what's your name?")
name=input()
print("Hello "+name+"! Guess a number between 1 and 50")
userNumber=int(input())
numberToGuess=random.randint(1,50)
while userNumber!=numberToGuess:
    if userNumber>numberToGuess:
        print("Your number is higher than mine try something else")
        userNumber=int(input())
    else:
        print("Your number is smaller than mine try something else")
        userNumber=int(input())
print("Good guess!")
