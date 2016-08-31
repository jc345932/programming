def calcItem(input):
    initial = int(input("Enter the initial stock:"))
    bought =  int(input("Enter how many we bought:"))
    sold = int(input("Enter how many we sold:"))
    total = initial + bought - sold
    return total
def main():
    totalCost = calcItem()
    print("The total cost of the product at the end of the day is ", totalCost)

main()