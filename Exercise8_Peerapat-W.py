print("Please, Enter your Username and Password")
userInput = input("Username :")
password = input("Password :")
if userInput == "admin" and password == "1234":
    print("----------------------")
    print("---Welcom To Apple shop---")
    print("please select an option below")
    apple = 10
    banana = 5
    mango = 15
    print("----------------------")
    print("option 1 = apple x 1  :", apple, "THB")
    print("option 2 = banana   x 1  :", banana, "THB")
    print("option 3 = mango x 1  :", mango, "THB")
    select = int(input("Option :"))

    if select == 1:
        item = "apple"
        number = int(input("Enter number of item :"))
        total = apple * number

    elif select == 2:
        item = "banana"
        number = int(input("Enter number of item :"))
        total = banana * number


    elif select == 3:
        item = "mango"
        number = int(input("Enter number of item :"))
        total = mango * number

    else:
        item = "Not found"
        number = 0
        total = 0
    print("-----------------------")

    print(item, "---------------", "x", number, "\ntotal =", total, "THB")
else: print("รหัสผ่านไม่ถูกต้องนะจ๊ะ")