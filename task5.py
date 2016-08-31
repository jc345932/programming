def workpay():
    hourlyrate = 24.95
    return  hourlyrate

def main():
    hour = int(input("Enter your work hour:"))
    pay = workpay()
    total = hour * pay

    print("Total pay is:", total)
main()