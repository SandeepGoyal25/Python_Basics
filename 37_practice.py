# x = 3
x = str('3')
print(type(x))

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)

x = "Python "
y = "is "
z = "awesome "
print(x+y+z)

x = "awesome"
def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)
myfunc()

print("Python is " + x)

x = frozenset({"apple", "banana", "cherry"})	
print(type(x))

x = b"Hello"
print(type(x))

x = list(["apple", "banana", "cherry"])	
print(type(x))

x = dict(name="John", age=36)
print(x)

x = 3+5j
y = -5j
print(type(x))
print(x+y)

import random
print(random.randrange(1, 10))

z = str(3.0)
print(z)
print(type(z))

a = "Hello, World!"
print(a[1])

x = "banana"
for x in "banana":
  print(x)
print(len(x))

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

b = "Hello,World! "
print(b.split(","))

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 33
s = "My name is Sandy, and I am {}"
print(s.format(age))

quantity = 15
item_no = 2
price = 19.5
myorder = "I want {} pieces of item {} for {} Rupees."
print(myorder.format(quantity, item_no, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \fVikings\f from the north."
print(txt)

txt = "banana"
x = txt.center(50)
print(x)

a = 'SANDY is a good guy'
print(a.center(4))

txt = "My name is Ståle"
x = txt.encode()
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
x =  txt.expandtabs(3)
x =  txt.expandtabs(4)
x =  txt.expandtabs(5)
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt3 = "My name is {0}, I'm {1}".format("John",36)
print(txt3)

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 200

if b>a:
    print("b is greater than a")
elif b==a:
    print("a is equal to b")
else:
    print("a is greater than b")

print(bool("Hello"))
print(bool())

class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(bool(myobj))

def myFunction():
    return False
print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 100
x += 10
y = 10
print(x)

x = 5

print(x > 4 and x < 7)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not y)

x = ["apple", "banana"]

print("mango" not in x)

thislist = ["apple", "mango", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(type(list1), list2, list3)

thislist = list(("apple", "banana", "cherry"))
print(thislist)
print(thislist[-2])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if 'cherry' in thislist:
    print("Yes, 'apple' is in the fruits list")