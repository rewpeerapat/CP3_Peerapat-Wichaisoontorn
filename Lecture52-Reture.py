totalPrice = int(input("TotalPrice: "))
Vat = int(input("TaxRate: "))
def vatCalculate(totalPrice):
    result = totalPrice+(totalPrice*Vat/100)
    return result

print(vatCalculate(totalPrice))
