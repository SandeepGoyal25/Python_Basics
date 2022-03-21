def sum(x, y):
    sum = x+y
    if sum in range(15,20):
        return 20
    else:
        return sum

print(sum(10,9))
print(sum(11,7))
print(sum(10,11))
print(sum(10,4))