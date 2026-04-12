import math

n = int(input("Enter a number: "))
rightmost_set_bit = n & -n
if rightmost_set_bit == 0:
    print("No set bits (input is 0)")
else:
    position = int(math.log2(rightmost_set_bit))
    print(f"Position of rightmost set bit: {position}")