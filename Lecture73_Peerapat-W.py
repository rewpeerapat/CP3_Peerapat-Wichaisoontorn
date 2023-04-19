systemMenu = {"ข้าวมันไก่": 45, "ข้าวหมกไก่": 40, "ข้าวมันไก่ผสม": 50, "ข้าวมันไก่พิเศษ": 50}
menuList = []

def showBill():
    total = 0
    print("----Your Bill----")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        total += int(menuList[number][1])
    print("Total:", total, "THB")

while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":
        break
    elif menuName in systemMenu:
        menuList.append([menuName, systemMenu[menuName]])
    else:
        print("Menu not found, please try again.")

showBill()