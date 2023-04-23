class Customer:
    name = ""
    lastname = ""
    age = 0
    def addCart(self):
        print("Added Product to",self.name,self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "Peerapat"
customer1.lastname = "W"
customer1.addCart()

customer2 = Customer()
customer2.name = "Minyada"
customer2.lastname = "B"
customer2.addCart()

customer3 = Customer()
customer3.name = "Thanaporn"
customer3.lastname = "N"
customer3.addCart()

customer4 = Customer()
customer4.name = "Kritipoom"
customer4.lastname = "P"
customer4.addCart()