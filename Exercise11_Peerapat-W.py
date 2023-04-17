number = int(input("Enter number: "))
for x in range(number):
    print(" "*(number-x),"*"*(x+1)+"*"*x)