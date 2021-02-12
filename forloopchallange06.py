num=int(input("enter number below 50"))
if num < 50:
    for i in range(50,num-1,-1):
        print(i)
    print("number was",num)
else:
    print("not below 50 ")
