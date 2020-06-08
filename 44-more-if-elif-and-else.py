answer=5

guess=int(input("Enter the number between 1 to 10."))


if guess<answer:
    print("Please guess higher.")
elif guess>answer:
    print("Pleaser guess lower.")
else:
    print("Your guess is correct...!!!")