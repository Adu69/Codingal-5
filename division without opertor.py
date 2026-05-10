def divide(ourDividend, ourDivisor):

    sign = (-1 if((ourDividend < 0) ^ (ourDivisor < 0)) else 1)

    ourDividend = abs(ourDividend)
    ourDivisor = abs(ourDivisor)

    quotientNumber = 0
    tempNumber = 0

    for i in range(31, -1, -1):
        if (tempNumber + (ourDivisor << i) <= ourDividend):
            tempNumber += ourDivisor << i
            quotientNumber |= 1 << i

    if (sign == -1):
        quotientNumber = -quotientNumber
    return quotientNumber

a = int(input("Enter the dividend: "))
b = int(input("Enter the divisor: "))
print("Quotient:", divide(a, b))