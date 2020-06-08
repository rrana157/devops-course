name=input("Enter your name:-")
age=int(input("How old are you, {0}? ".format(name)))
print(age)


if age >=18:
    print("You are old enough to vote.")
else:
    print("Please, come back in {0} years.".format(18-age))