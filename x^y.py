def computePower(x,y):

    result = 1

    while(y > 0):
        if (y % 2 == 0):
            x = x * x
            y >>= 1
        else:
            result = result * x
            y -= 1

    return result

x = int(input("Enter the base: "))
y = int(input("Enter the exponent: "))
print(f"{x} raised to the power of {y} is: {computePower(x,y)}")