num=int(input("enter number betwwen 1 and 12"))
if num >=1 and num <=12:
    for i in range(0,(num*13),num):
        print(i)
else:
    print("not between 1 and 12")
