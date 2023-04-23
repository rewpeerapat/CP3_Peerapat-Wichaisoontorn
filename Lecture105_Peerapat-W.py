class Vehicle:
	licenseNo = ""
	serialNo = ""
	def turnOnAirContioner(self, x):
		print(x, ": Air : Turn ON")

class Car(Vehicle):
	pass

class Pickup(Vehicle):
	pass

class Van(Vehicle):
	pass

class Estatecar(Vehicle):
	pass

car1 = Car()
car1.turnOnAirContioner("Car")

pickup1 = Pickup()
pickup1.turnOnAirContioner("Pickup")

van1 = Van()
van1.turnOnAirContioner("Van")

estateCar1 = Estatecar()
estateCar1.turnOnAirContioner("Esatate Car")