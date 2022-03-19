# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# sum = a+b+c
# print(sum)

def sum_thrice(x, y, z):
    sum = x + y + z
    if x==y==z:
        sum = sum*3
    return sum

print(sum_thrice(1,2,3))
print(sum_thrice(3,3,3))