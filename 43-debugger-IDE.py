name=input("Enter your name:-")
age=int(input("How old are you, {0}?".format(name)))

print(age)



if age <18 :
    print("Please come back in {0} years.".format(18-age))
elif age == 900:
    print("You are kidding to us.")
else:
    print("You are old enough to vote.")
    
    