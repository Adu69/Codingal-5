def printTwoOdd(arr, size):
    xorof2 = arr[0]

    x = 0
    y = 0

    Set_bit = 0
    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]

    Set_bit = xorof2 & ~(xorof2 - 1)

    for i in range(size):
        if (arr[i] & Set_bit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    print("The two odd elements are {} and {}".format(x, y))

arr = []
size = int(input("Enter the size of the array: "))
print("Enter the elements of the array: ")
for i in range(size):
    element = int(input())
    arr.append(element)
printTwoOdd(arr, size)
