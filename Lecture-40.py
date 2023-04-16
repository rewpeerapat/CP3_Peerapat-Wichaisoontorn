usernameInput = input("username : ")
passwordInput = input("password : ")
if usernameInput == "admin" and passwordInput == "1234":
    print("Done !!")
    print("----iShop----")
    print("1. Vat calculator")
    print("2. Price Calculator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("price(THB) : "))
        vat = 7
        result = price + (price*vat/100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Goods Price"))
        price2 = int(input("Second Goods Price"))
        print(price1+price2)
else : print("Wrong Username or password!!!")

