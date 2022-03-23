a = {1, 2, 3, 4, 5}
print(type(a))
print(a)
b = {} # create empty dictionary 
c = set() #creating empty set
print(type(c))

c.add(0)
c.add(5) #adding 5 to set
# c.add({1:2}) #cant add dict to set
print(c)
print(len(c)) # length of c
# c.remove(5) #removes 5 from set
print(c)
c.pop()
print(c)