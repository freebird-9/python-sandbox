# from datetime import time

# x = time(hour=15)

# print(x)


# y = ['apple', 'oranges', 'kiwi']

# del(y[1])

# print(y)

# x = False
# print(not x)

# x = 2

# while x < 9:
#   print(x)
#   x +=1

# import calendar as c
# print(c.month_name[7])

# for i in range(-9,9):
#     if i > 0:
#      print("graeter than 0")
#     elif i == 0:
#      print("equals to zero")
#     else:
#      print("whatever")

# def myfunction():
#   global x
#   x = 'Hello'

# myfunction()

# print(x)

# x = "Hello"

# assert x == "Hello"

# assert x == " goodbye", "x should be 'Hello'"

# a = 20
# b = 30
# if a > b:
#   pass

# for i in range(9):
#   if i > 5:
#       break
#   print(i)

# 

# class person:
#   age = 26
#   name = "shaka"

# x = "hello"

# if not type(x) is int:
#   raise TypeError("only integers are allowed")

# x = ["apple", "banana", "cherry"]

# y = ["apple", "banana", "cherry"]

# y = x

# print(x is y)
# print("x-------->", x)
# print("y-------->", y)
# y = x
# print(y)
# if x == y: 
#   print("true")
# else:
#   print("false")

# Normal function
def normal_test():
    return "Hello World"
	
#Generator function
def generator_test():
	yield "Hello World"
print(normal_test()) #call to normal function
print(generator_test()) # call to generator function
print(next(generator_test()))