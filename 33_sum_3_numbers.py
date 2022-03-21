# a = 4
# b = 5
# c = 6
# print(a+b+c)
def sum(x, y, z):
    if x == y or y == z or x == z:
        sum = 0
    else:
        sum = x+y+z
    return sum

print(sum(1,2,1))
print(sum(11,2,1))
print(sum(44, 55, 55))
print(sum(100,200,10))