menuList = []
priceList = []
def showBill():
    print("----My bill----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
    print("Total :",sum(priceList),"THB")

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(float(menuPrice))

showBill()

