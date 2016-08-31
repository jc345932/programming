def main():

    x = int(input("Enter x:"))
    y = int(input("Enter y:"))
    doMath(x, y)

def doMath (x, y):
    sum = x + y
    diff = x - y
    product = x * y
    quotient = x / y

    print(sum)
    print(diff)
    print(product)
    print(quotient)

main()