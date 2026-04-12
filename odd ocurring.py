def OddOcurring(arr):

    res = 0

    for element in arr:
        res = res ^ element

    return res

arr = []

n = int(input("Enter the number of elements in the array: "))

while(n):
    num = int(input("Enter the element: "))
    arr.append(num) 
    n-=1

print("The odd occurring element is: ", OddOcurring(arr))