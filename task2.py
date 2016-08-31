def getFuel(dist,fuelCon):
    fuelNeeded = (dist * fuelCon) / 100
    return fuelNeeded

def main():

    distance = int(input("Enter the distance:"))
    fuelCon = int(input("Enter the fuel consumption:"))
    fuel = getFuel(distance, fuelCon)
    print("Fuel needed is :", fuel)
main()