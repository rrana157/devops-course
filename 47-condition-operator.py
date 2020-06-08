answer=5

print("guess the number between 1 to 10.\n")
guess=int(input())


if guess==answer:
    print("You got it first time.")

elif guess!=answer:
    if guess>answer:
        print("guess the number lower")
    else:
        print("guess the number higher")
    guess=int(input())
    if guess==answer:
        print("well done, you guessed it.")
    else:
        print("sorry, you have not guessed correctly.")


# if guess!=answer:
#     if guess>answer:
#         print("guess the number lower")
#     else:
#         print("guess the number higher")
#     guess=int(input())
#     if guess==answer:
#         print("Well done, you guessed it.")
#     else:
#         print("sorry you have not guessed correctly.")
# else:
#     print("You got it  first time.")
  
            