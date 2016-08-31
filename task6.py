def getDiscount(price):
    discount = price * 0.2
    return discount
def main():
    price = int(input("Enter the items price:"))
    disc = getDiscount(price)
    totalpay = price - disc
    day = "Monday"
    result = "Today is {}, my pocket money is ${:.2f}." .format(day,totalpay )
    print(result)
main()
