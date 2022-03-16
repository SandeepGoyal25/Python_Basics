# a = int(input("Enter num1 a: "))
# b = int(input("Enter num2 b: "))
# c = int(input("Enter num3 c: "))
# d = int(input("Enter num4 d: "))

# list1 = ['a', 'b', 'c', 'd']
# print("add item in list1")
values = input("Enter some comma seperated numbers: ")
list = values.split(",")
tuple = tuple(list)
print("list: ", list)
print("Tuple: ", tuple)