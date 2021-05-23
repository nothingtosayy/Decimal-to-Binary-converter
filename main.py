# Decimal to Binary Converter

def decimaltobinary(n):
    binary = ""
    if n == 0:
        return 0
    while n != 0:
        rem = n%2
        quotient = n//2
        binary = str(rem) + binary
        n = quotient
    return binary
n = int(input())
print(f"The binary form of {n} is: {decimaltobinary(n)}")

# Binary to Decimal
# e.g: num = 0b101
# print(n) 
# output : 5
