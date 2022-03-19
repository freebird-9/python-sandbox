ten_things = "Apples Oranges Crows Telephone Light Sugar" #defining a string

print("Wait there's not 10 things in that list, let's fix that.") #printing aline

stuff = ten_things.split(' ') #spliting string into list of items
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"] #defining a list

while len(stuff) != 10: # initiating a while loop end cond is till length is not equal to 10
    next_one = more_stuff.pop() #poping last value from list and puting hat into variable named next_one
    print("Adding:", next_one) #printing
    stuff.append(next_one) #adding next_one variable to stuff
    print("There's %d items now." %len(stuff))
    
print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) 
print('#'.join(stuff[3:5]))
