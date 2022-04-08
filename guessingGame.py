# Cooper Myers
# Python Program for User to Guess Number Stored

answer = 3
print("Please guess an integer input between 0-3: ")
guess = int(input())

if guess == answer:
        print("*FIRST TRY!*")

elif guess < answer:
    print("Sorry, guess higher.")
    guess = int(input())

elif guess > answer:
    print("Sorry, guess lower.")
    guess = int(input())

else:
    print("INVALID USER INPUT.")

print("Well done, you guessed it!")
