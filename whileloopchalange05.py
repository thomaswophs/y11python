compnum=50
num=int(input("enter new number"))
count=1
while num != compnum:
    if num >= compnum:
        print("too high")
    else:
        print("too low")
    num=int(input("new number"))
    count=count+1
print("congrats it only took",count,"atempts")
# made by thomas while loop challange 05
