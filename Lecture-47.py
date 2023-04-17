#number = int(input("Enter number: "))
#text = ""
#for i in range(number):
#    text = text+"*"
#print(text)

number = int(input("Enter number: "))
for x in range(number):
    print(" "*(number-x),"*"*(x+1)+"*"*x)