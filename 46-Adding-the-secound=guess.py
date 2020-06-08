answer=5

print("Please guess the number between 1 to 10:")
guess=int(input())


if guess>answer:
    print("Please guess lower.")
    guess=int(input())
    if guess == answer:
        print("Well done, You guessed it.")
    else:
        print("sorry, you have not guessed correctly.")

elif guess<answer:
    print("Please guess higher.")
    guess=int(input())
    if guess == answer:
        print("Well done, You guessed it.")
    else:
        print("sorry, you have not guessed correctly.")
else:
    print("Well done, You guessed it.")