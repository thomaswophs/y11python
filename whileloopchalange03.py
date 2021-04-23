num1=int(input("enter a number"))
total=num1
answer="y".lower()
while answer == "y":
    num2=int(input("enter a second number"))
    total=num1+num2
    answer=input("do you want to add another number").lower()
print("your total is",total,"")
# made by thomas while loop challange 03
