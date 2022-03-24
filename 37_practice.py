# x = 3
x = str("3")
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
b = 20
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
x = 2
print(x > 4 and x < 7)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = ["apple", "banana"]
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
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# from re import 
thislist_1 = ["apple", "banana", "cherry"]
thislist_2 = ["mango", "pineapple", "papaya"]
thistuple = ("kiwi", "orange")
thislist_1.extend(thistuple)
print(thislist_1)
thislist_1.remove("cherry")
print(thislist_1)
thislist_1.pop(1)
print(thislist_1)
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# from hashlib import ne
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
# from hashlib import ne
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
newlist = [x for x in fruits if x != "apple"]
newlist = [x for x in range(10)]
newlist = [x for x in fruits]
newlist = [x for x in range(10) if x < 5]
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
thislist = ["apple", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
thislist = ["apple", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1+list2
print(list3)
for x in list2:
    list1.append(x)
print(list1)
list1.extend(list2)
print(list1)
L1 = (("apple", "banana", "cherry"))
print(type(L1))
a = 8
print(type(a))
thisTuple = tuple(("apple", "cherry", "banana", "cherry"))
if "apple" in thisTuple:
    print("Yes", "apple is present")
x = ("apple", "banana", "cherry")
y = list(x)
y.append("kiwi")
x = tuple(y)
print(x)
x = ("apple", "banana", "cherry")
y = ("orange", "mango")
x += y
print(x)
x = ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
thistuple  = ('apple', 'banana', 'cherry', 'orange', 'mango')
del thistuple
# print(thistuple)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, *red, yellow) = fruits
print(green)
print(yellow)
print(red)
thistuple = ("cherry", "strawberry", "raspberry", "cherry")
for x in thistuple:
    print(x)
thistuple = ("cherry", "strawberry", "raspberry", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])
x = ("apple", "banana", "cherry")
y = ("cherry", "strawberry", "raspberry", "cherry")
z = x+y
print(z)
fruits = ('cherry', 'strawberry', 'raspberry', 'cherry', 'cherry', 'strawberry', 'raspberry', 'cherry')
x = fruits.index("strawberry")
print(x)
myset = {"apple", "cherry", "banana", "cherry"}
print(type(myset))
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
a = {'cherry', 'strawberry', 'raspberry', "banana", 'cherry', 'cherry', 'strawberry', 'raspberry', 'cherry'}
for x in a:
    print(x)
print("banana" in a)
a.add("orange")
print(a)
b = tropical = {"pineapple", "mango", "papaya"}
a.update(b)
print(a)
a = {"pineapple", "mango", "papaya"}
b = ["apple", "banana", "cherry"]
print(type(a))
print(type(b))
a.update(b)
print(a)
# import this
thisSet = {"pineapple", "mango", "papaya"}
thisSet.remove("pineapple")
print(thisSet)
thisSet = {"pineapple", "mango", "papaya"}
thisSet.discard("Banana")                    # Will not give an error
print(thisSet)
thisSet = {"pineapple", "mango", "papaya"}
x = thisSet.pop()
print(x)
print(thisSet)
thisSet = {"pineapple", "mango", "papaya"}
thisSet.clear()
print(thisSet)
# from re import 
a = {"apple", "banana", "cherry"}
del a
# print(a)
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set2.union(set1)
set3 = set1.union(set2)
print(set3)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3, 5}
set1.update(set2)
print(set1)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])
# om operator import l
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2000
}
print(thisdict)
print(len(thisdict))
MyDict = {
    'brand' : "Ford",
    "electric" : False,
    "model" : 'Figo Aspire',
    'make' : 201
}
print(MyDict)
print(type(MyDict))
x = MyDict['make']
y = MyDict.get('electric')
z = MyDict.values()
a = MyDict.keys()
print(x)
print(y)
print(z)
print(a)
MyCar = {
"brand": "Ford",
"model": "Figo Aspire",
"year": 2017
}
x = MyCar.keys()
print(x)
MyCar["color"] = "Silver"
print(x)
print(MyCar)
MyCar = {
"brand": "Ford",
"model": "Figo Aspire",
"year": 2017
}
x = MyCar.values()
print(x)
MyCar["color"] = "Silver"
print(x)
print(MyCar)
print(MyCar.items())
MyCar = {
"brand": "Ford",
"model": "Figo Aspire",
"year": 2017
}
x = MyCar.items()
print(x)
MyCar['year'] = 2020
print(x)
MyCar['color'] = 'Silver'
print(x)
print(MyCar.items())
MyCar = {
"brand": "Ford",
"model": "Figo Aspire",
"year": 2017
}
if "model" in MyCar:
    print("Yes, 'model' is one of the keys in the MyCar dictionary")
if "color" in MyCar:
    print("No, 'color' is one of the keys in the MyCar dictionary")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2017
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year" : 2017})
print(thisdict)
thisdict.update({"color" : "Silver"})
print(thisdict)
MyDict = {
"Job" : "Engineering",
"UPSC" : "Preparation",
}
print(MyDict)
MyDict["Python"] = "Practice"
MyDict["From"] = "Feb 2022 to Mar 2022"
print(MyDict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["brand"]
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
# print(thisdict)
thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964 }
for x in thisdict.values():
    print(x)
    # print(thisdict[x])
for x in thisdict.keys():
    print(x)
for x, y in thisdict.items():
    print(x,y)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
myDict = thisdict.copy()
print(myDict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
myDict = dict(thisdict)
print(myDict)
myfamily = {
  "child1" : {
    "name" : "Vihaan",
    "year" : 2012
  },
  "child2" : {
    "name" : "Suhani",
    "year" : 2013
  },
  "child3" : {
    "name" : "Shaurya",
    "year" : 2018
  },
  "child4" : {
    "name" : "Innaya",
    "year" : 2018
  },
  "child5" : {
    "name" : "Shreyansh",
    "year" : 2021
  }
}
print(myfamily)
child1 = {
    "name": "Vihaan",
    "year": 2012
},
child2 = {
    "name": "Suhani",
    "year": 2013
},
child3 = {
    "name": "Shaurya",
    "year": 2018
},
child4 = {
    "name": "Innaya",
    "year": 2018
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3,
  "child4" : child4
}
print(myfamily)
a = 33
b = 200
if b > a:
    print("b is greater than a")
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
a = 100
b = 99
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
a = 100
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
a = 100
b = 33
if a > b: print("a is greater than b")
a = 1
b = 303
print("a") if a > b else print("b")
a = 303
b = 303
print("a") if a > b else print("=") if a == b else print("b")
a = 300
b = 200
c = 500
if a > b and c > a:
    print("Both conditions are True")
a = 300
b = 200
c = 500
if a > b or c < a:
    print("At least one of the conditions is True")
x = 40
if x > 10:
    print("Above 10,")
    if x > 20:
        print("and above 20!")
    else:
        print("but not above 20.")
a = 100
b = 200
if b>a:
    pass