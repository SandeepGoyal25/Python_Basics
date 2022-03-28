# # x = 3
# x = 3
# print(type(x))
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0
# print(x)
# x = "Python "
# y = "is "
# z = "awesome "
# print(x+y+z)
# x = "awesome"
# def myfunc():
#     global x
#     x = "fantastic"
#     print("Python is " + x)
# myfunc()
# print("Python is " + x)
# x = frozenset({"apple", "banana", "cherry"})
# print(type(x))
# x = b"Hello"
# print(type(x))
# x = list(["apple", "banana", "cherry"])
# print(type(x))
# x = dict(name="John", age=36)
# print(x)
# x = 3+5j
# y = -5j
# print(type(x))
# print(x+y)
# import random
# print(random.randrange(1, 10))
# z = str(3.0)
# print(z)
# print(type(z))
# a = "Hello, World!"
# print(a[1])
# x = "banana"
# for x in "banana":
#   print(x)
# print(len(x))
# a = "Hello, World!"
# print(len(a))
# txt = "The best things in life are free!"
# print("free" in txt)
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")
# txt = "The best things in life are free!"
# print("expensive" not in txt)
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")
# b = "Hello,World! "
# print(b.split(","))
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)
# age = 33
# s = "My name is Sandy, and I am {}"
# print(s.format(age))
# quantity = 15
# item_no = 2
# price = 19.5
# myorder = "I want {} pieces of item {} for {} Rupees."
# print(myorder.format(quantity, item_no, price))
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))
# txt = "We are the so-called \fVikings\f from the north."
# print(txt)
# txt = "banana"
# x = txt.center(50)
# print(x)
# a = 'SANDY is a good guy'
# print(a.center(4))
# txt = "My name is Ståle"
# x = txt.encode()
# print(x)
# txt = "H\te\tl\tl\to"
# x =  txt.expandtabs(2)
# x =  txt.expandtabs(3)
# x =  txt.expandtabs(4)
# x =  txt.expandtabs(5)
# print(x)
# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x)
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))
# txt3 = "My name is {0}, I'm {1}".format("John",36)
# print(txt3)
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)
# a = 200
# b = 20
# if b>a:
#     print("b is greater than a")
# elif b==a:
#     print("a is equal to b")
# else:
#     print("a is greater than b")
# print(bool("Hello"))
# print(bool())
# class myclass():
#     def __len__(self):
#         return 0
# myobj = myclass()
# print(bool(myobj))
# def myFunction():
#     return False
# print(myFunction())
# def myFunction() :
#   return True
# if myFunction():
#   print("YES!")
# else:
#   print("NO!")
# x = 100
# x += 10
# y = 10
# print(x)
# x = 2
# print(x > 4 and x < 7)
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = ["apple", "banana"]
# print(x is not y)
# x = ["apple", "banana"]
# print("mango" not in x)
# thislist = ["apple", "mango", "cherry"]
# print(thislist)
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(len(thislist))
# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]
# print(type(list1), list2, list3)
# thislist = list(("apple", "banana", "cherry"))
# print(thislist)
# print(thislist[-2])
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# if 'cherry' in thislist:
#     print("Yes, 'apple' is in the fruits list")
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
# # from re import 
# thislist_1 = ["apple", "banana", "cherry"]
# thislist_2 = ["mango", "pineapple", "papaya"]
# thistuple = ("kiwi", "orange")
# thislist_1.extend(thistuple)
# print(thislist_1)
# thislist_1.remove("cherry")
# print(thislist_1)
# thislist_1.pop(1)
# print(thislist_1)
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]
# # from hashlib import ne
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)
# # from hashlib import ne
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)
# newlist = [x for x in fruits if x != "apple"]
# newlist = [x for x in range(10)]
# newlist = [x for x in fruits]
# newlist = [x for x in range(10) if x < 5]
# newlist = [x.upper() for x in fruits]
# newlist = ['hello' for x in fruits]
# newlist = [x if x != "banana" else "orange" for x in fruits]
# print(newlist)
# thislist = ["apple", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
# thislist = ["apple", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)
# def myfunc(n):
#     return abs(n - 50)
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1+list2
# print(list3)
# for x in list2:
#     list1.append(x)
# print(list1)
# list1.extend(list2)
# print(list1)
# L1 = (("apple", "banana", "cherry"))
# print(type(L1))
# a = 8
# print(type(a))
# thisTuple = tuple(("apple", "cherry", "banana", "cherry"))
# if "apple" in thisTuple:
#     print("Yes", "apple is present")
# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("kiwi")
# x = tuple(y)
# print(x)
# x = ("apple", "banana", "cherry")
# y = ("orange", "mango")
# x += y
# print(x)
# x = ("apple", "banana", "cherry")
# y = list(x)
# y.remove("apple")
# x = tuple(y)
# print(x)
# thistuple  = ('apple', 'banana', 'cherry', 'orange', 'mango')
# del thistuple
# # print(thistuple)
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, *red, yellow) = fruits
# print(green)
# print(yellow)
# print(red)
# thistuple = ("cherry", "strawberry", "raspberry", "cherry")
# for x in thistuple:
#     print(x)
# thistuple = ("cherry", "strawberry", "raspberry", "cherry")
# for i in range(len(thistuple)):
#     print(thistuple[i])
# x = ("apple", "banana", "cherry")
# y = ("cherry", "strawberry", "raspberry", "cherry")
# z = x+y
# print(z)
# fruits = ('cherry', 'strawberry', 'raspberry', 'cherry', 'cherry', 'strawberry', 'raspberry', 'cherry')
# x = fruits.index("strawberry")
# print(x)
# myset = {"apple", "cherry", "banana", "cherry"}
# print(type(myset))
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# print(thisset)
# a = {'cherry', 'strawberry', 'raspberry', "banana", 'cherry', 'cherry', 'strawberry', 'raspberry', 'cherry'}
# for x in a:
#     print(x)
# print("banana" in a)
# a.add("orange")
# print(a)
# b = tropical = {"pineapple", "mango", "papaya"}
# a.update(b)
# print(a)
# a = {"pineapple", "mango", "papaya"}
# b = ["apple", "banana", "cherry"]
# print(type(a))
# print(type(b))
# a.update(b)
# print(a)
# # import this
# thisSet = {"pineapple", "mango", "papaya"}
# thisSet.remove("pineapple")
# print(thisSet)
# thisSet = {"pineapple", "mango", "papaya"}
# thisSet.discard("Banana")                    # Will not give an error
# print(thisSet)
# thisSet = {"pineapple", "mango", "papaya"}
# x = thisSet.pop()
# print(x)
# print(thisSet)
# thisSet = {"pineapple", "mango", "papaya"}
# thisSet.clear()
# print(thisSet)
# # from re import 
# a = {"apple", "banana", "cherry"}
# del a
# # print(a)
# thisset = {"apple", "banana", "cherry"}
# for x in thisset:
#     print(x)
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set3 = set2.union(set1)
# set3 = set1.union(set2)
# print(set3)
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3, 5}
# set1.update(set2)
# print(set1)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = x.issubset(y)
# print(z)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)
# print(thisdict["brand"])
# # om operator import l
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2000
# }
# print(thisdict)
# print(len(thisdict))
# MyDict = {
#     'brand' : "Ford",
#     "electric" : False,
#     "model" : 'Figo Aspire',
#     'make' : 201
# }
# print(MyDict)
# print(type(MyDict))
# x = MyDict['make']
# y = MyDict.get('electric')
# z = MyDict.values()
# a = MyDict.keys()
# print(x)
# print(y)
# print(z)
# print(a)
# MyCar = {
# "brand": "Ford",
# "model": "Figo Aspire",
# "year": 2017
# }
# x = MyCar.keys()
# print(x)
# MyCar["color"] = "Silver"
# print(x)
# print(MyCar)
# MyCar = {
# "brand": "Ford",
# "model": "Figo Aspire",
# "year": 2017
# }
# x = MyCar.values()
# print(x)
# MyCar["color"] = "Silver"
# print(x)
# print(MyCar)
# print(MyCar.items())
# MyCar = {
# "brand": "Ford",
# "model": "Figo Aspire",
# "year": 2017
# }
# x = MyCar.items()
# print(x)
# MyCar['year'] = 2020
# print(x)
# MyCar['color'] = 'Silver'
# print(x)
# print(MyCar.items())
# MyCar = {
# "brand": "Ford",
# "model": "Figo Aspire",
# "year": 2017
# }
# if "model" in MyCar:
#     print("Yes, 'model' is one of the keys in the MyCar dictionary")
# if "color" in MyCar:
#     print("No, 'color' is one of the keys in the MyCar dictionary")
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2017
# print(thisdict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year" : 2017})
# print(thisdict)
# thisdict.update({"color" : "Silver"})
# print(thisdict)
# MyDict = {
# "Job" : "Engineering",
# "UPSC" : "Preparation",
# }
# print(MyDict)
# MyDict["Python"] = "Practice"
# MyDict["From"] = "Feb 2022 to Mar 2022"
# print(MyDict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["brand"]
# print(thisdict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# # print(thisdict)
# thisdict = {  "brand": "Ford",  "model": "Mustang",  "year": 1964 }
# for x in thisdict.values():
#     print(x)
#     # print(thisdict[x])
# for x in thisdict.keys():
#     print(x)
# for x, y in thisdict.items():
#     print(x,y)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# myDict = thisdict.copy()
# print(myDict)
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# myDict = dict(thisdict)
# print(myDict)
# myfamily = {
#   "child1" : {
#     "name" : "Vihaan",
#     "year" : 2012
#   },
#   "child2" : {
#     "name" : "Suhani",
#     "year" : 2013
#   },
#   "child3" : {
#     "name" : "Shaurya",
#     "year" : 2018
#   },
#   "child4" : {
#     "name" : "Innaya",
#     "year" : 2018
#   },
#   "child5" : {
#     "name" : "Shreyansh",
#     "year" : 2021
#   }
# }
# print(myfamily)
# child1 = {
#     "name": "Vihaan",
#     "year": 2012
# },
# child2 = {
#     "name": "Suhani",
#     "year": 2013
# },
# child3 = {
#     "name": "Shaurya",
#     "year": 2018
# },
# child4 = {
#     "name": "Innaya",
#     "year": 2018
# }
# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3,
#   "child4" : child4
# }
# print(myfamily)
# a = 33
# b = 200
# if b > a:
#     print("b is greater than a")
# a = 33
# b = 33
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# a = 100
# b = 99
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")
# a = 100
# b = 33
# if b > a:
#     print("b is greater than a")
# else:
#     print("b is not greater than a")
# a = 100
# b = 33
# if a > b: print("a is greater than b")
# a = 1
# b = 303
# print("a") if a > b else print("b")
# a = 303
# b = 303
# print("a") if a > b else print("=") if a == b else print("b")
# a = 300
# b = 200
# c = 500
# if a > b and c > a:
#     print("Both conditions are True")
# a = 300
# b = 200
# c = 500
# if a > b or c < a:
#     print("At least one of the conditions is True")
# x = 40
# if x > 10:
#     print("Above 10,")
#     if x > 20:
#         print("and above 20!")
#     else:
#         print("but not above 20.")
# a = 100
# b = 200
# if b>a:
#     pass
# i = 1
# while i < 5:
#   print(i)
#   i += 1
# i = 1
# while i < 7:
#   print(i)
#   if i == 4:
#     break
#   i += 1
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
# for x in "banana":
#   print(x)
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":
#     break
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x) 
# for x in range(5, 100, 10):
#   print(x)
# for x in range (7):
#   if x == 3: break
#   print(x)
# else:
#   print("Thus finished!")
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#   for y in fruits:
#     print(x, y)
# for x in [0, 1, 2]:
#   pass
# def my_function():
#     print("Hello from a function")
# my_function()
# def my_function(fname):
#     print(fname + " Gupta")
# my_function("Vihaan")
# my_function("Suhaani")
# my_function("Shreyansh")
# def my_function(Fname, Lname):
#     print(Fname + " " + Lname)
# my_function("Shreyansh", "Goyal")
# def my_func(*kids):
#     print("The youngest child is " + kids[2])
# my_func("Innaya", "Shaurya", "Shreyansh")
# def my_func(child3, child2, child1):
#     print("The youngest child is " + child3)
# my_func(child1 = "Innaya", child2 = "Shaurya", child3= "Shreyansh")
# def my_func(**kid):
#     print("His first name is " + kid["fname"])
# my_func(fname = "Shreyansh", lname = "Goyal", mname = "Sandeep")
# def my_func(country = "India"):
#     print("I am from " + country)
# my_func("China")
# my_func("USA")
# my_func("Japan")
# my_func()
# # om cgitb import reset
# # om operator import ne
# # om statistics import multimode
# # om traceback import FrameSummary
# # om unittest import result
# def my_func(food):
#     for x in food:
#         print(x)
# Fruits = ['apple', 'banana', "mango"]
# my_func(Fruits)
# def my_function(x):
#     return 5 * x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
# def function():
#     pass
# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result
# print("\n\Recursion Example Results")
# tri_recursion(6)
# x = lambda a : a + 10
# print(x(10))
# x = lambda a, b: a*b
# print(x(8, 9))
# x = lambda a, b, c : a+b+c
# print(x(4, 5, 6))
# def my_func(n):
#     return lambda a: a*n
# mydoubler = my_func(2)
# print(mydoubler(19))
# def my_func(n):
#     return lambda a: a*n
# mytripler = my_func(3)
# print(mytripler(19))
# cars = ["Ford", "Volvo", "BMW"]
# print(type(cars))
# x = cars[1]
# print(x)
# cars[1] = "Toyota"
# print(cars)
# x = len(cars)
# print(x)
# for x in cars:
#     print(x)
# cars.append("Honda")
# print(cars)
# cars.pop(2)
# x = cars.index("Honda")
# print(x)
# class MyClass:
#     x = 5
#     print(x)
# class MyClass:
#      x = 5
# p1 = MyClass()
# print(p1.x)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p1 = Person("Sandy", 33)
# print(p1.name)
# print(p1.age)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def myfunc(self):
#         print("Hello my name is " + self.name)
# p1 = Person("Sandy", 33)
# p1.myfunc()
# class Person:
#     def __init__(mysillyobject, name, age):
#         mysillyobject.name = name
#         mysillyobject.age = age
#     def myfunc(abc):
#         print("Hello my name is " + abc.name)
# p1 = Person("Sandy", 33)
# p1.age = 30
# p1.myfunc()
# print(p1.age)
# del p1.age
# # print(p1.age)
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#     def printname(self):
#         print(self.firstname, self.lastname)
# # x = Person("Sandy", "Goyal")
# # x.printname()
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = 2021
#         # Person.__init__(self, fname, lname)
#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
# x = Student("Shrey", "Goyal", 2021)
# x.welcome()
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# mystr = "banana"
# myit = iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# mytuple = ("apple", "banana", "cherry")
# for x in mytuple:
#     print(x)
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
# myclass = MyNumbers()
# myiter = iter(myclass)
# for x in myiter:
#     print(x)
# from inspect import modulesbyfile
# def myfunc():
#     x = 300
#     print(x)
# myfunc()
# def myfunc():
#     x = 300
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()
# myfunc()
# x = 300
# def myfunc():
#     x = 200
#     print(x)
# myfunc()
# print(x)
# def myfunc():
#     global x 
#     x = 200
# myfunc()
# print(x)
# x = 300
# def myfunc():
#     global x
#     x = 200
# myfunc()
# print(x)
# import mymodule
# a = mymodule.person1["city"]
# print(a)
# import mymodule as mx
# a = mx.person1["name"]
# print(a)
# import platform
# x = platform.system()
# print(x)
# import imp
# import platform
# x = dir(platform)
# print(x)
# from mymodule import person1
# print (person1["city"])
# import datetime
# x = datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.month)
# print(x.strftime("%A"))
# print(x.strftime("%B"))
# print(x.strftime("%I"))
# print(x.strftime("%H"))
# print(x.strftime("%p"))
# print(x.strftime("%z"))
# print(x.strftime("%Z"))
# print(x.strftime("%M"))
# print(x.strftime("%j"))
# print(x.strftime("%U"))
# print(x.strftime("%x"))
# import datetime
# x = datetime.datetime(2020, 1, 25)
# print(x)
# x = min(5, 10, 25)
# y = max(5, 10, 25)
# print(x)
# print(y)
# x = abs(-9.076)
# print(x)
# x = pow(4, 3)
# print(x)
# import math
# x = math.sqrt(64)
# print(x)
# import math
# x = math.ceil(1.4)
# y = math.floor(1.4)
# print(x)
# print(y)
# x = math.pi
# print(x)
# import json
# #### some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# #### parse x:
# y = json.loads(x)
# #### the result is a Python dictionary:
# print(y["age"])
# import json
# ### a Python object (dict):
# x = {
#     "name" : "Sandeep",
#     "age" : 33,
#     "city" : "Gurgaon"
# }
# ### convert into JSON:
# y = json.dumps(x)
# ### the result is a JSON string:
# print(y)
# print(type(y))
# import json
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# # When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
# # 
# # Python	JSON
# # dict	Object
# # list	Array
# # tuple	Array
# # str	    String
# # int   	Number
# # float	Number
# # True	true
# # False	false
# # None	null

# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x))
# print(json.dumps(x, indent=4))
# print(json.dumps(x, indent=4, separators=(". ", " = ")))
# print(json.dumps(x, indent=4, sort_keys=True))
# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#     print("Yes! We have a match 😊")
# else:
#     print("No match 😒")
# import re
# txt = "The rain in Spain"
# #Check if "Portugal" is in the string:
# x = re.findall("Portugal", txt)
# print(x)
# if (x):
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
# import re
# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)
# import re
# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)
# print(x)
# import re
# txt = "The rain in Spain "
# x = re.sub("\s", "* ", txt)
# print(x)
# import re
# txt = "The rain in Spain "
# x = re.sub("\s", "* ", txt, 2)
# print(x)
# import re
# txt = "The rain in Spain"
# x = re.search(r"\bS\w+", txt)
# print(x.span())
# import camelcase

# try:
#     print(x)
# except:
#     print("An exception occured")

# print(x)


# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero")

# x = "hello"
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")

# username = input("Enter username: ")
# print("Username is: " + username)

# price = 50
# txt = "The price is {:.2f} rupees"
# print(txt.format(price))

# age = 32
# name = "Sandeep"
# txt = "His name is {1}. {1} is {0} years old."
# print(txt.format(age, name))

# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname = "Ford", model = "Figo Aspire(2017)"))