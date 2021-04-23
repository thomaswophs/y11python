number=int(input("a number between 10 and 20"))
while number < 10 or number > 20:
    if number < 10:
        print("too low try again")
        number=int(input("try again"))
    elif number >20:
        print("too high")
        number=int(input("try again"))
print("thank you")
# made by thomas while loop challange 06
