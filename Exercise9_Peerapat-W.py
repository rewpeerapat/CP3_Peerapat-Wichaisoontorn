userName = input("userName: ")
password = input("password: ")
while userName != "admin" or password != "1234":
    print("---------")
    userName = input("userName: ")
    password = input("password: ")
print("Connect")