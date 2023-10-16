import random
import time

user_guess = int()
guess = int ()
counter = 0


print("Pick a Number between 1 and 10 and I will Try And Guess Your Number")

user_guess = int(input("What is Your Number ?"))

for counter in range (10):
    counter += 1 
    guess = random.randint(1,10)
    if guess == user_guess:
        print(f"Your Number is {guess} ! ")
        break
    else:
        print(f"Is Your Number {guess}")
        time.sleep(1)
        print("No...... That's Not it")

if counter == 10 and guess!= user_guess:
    print("You Win i Cant Guess It !")


if user_guess > 10:
    print("I Know You Cheated -_____-")