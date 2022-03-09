def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("subtracting %d - %d" %(a, b))
    return a-b
    
def multiply(a, b):
     print("Multiply %d %d " %(a, b))
     return a*b
     
def divide(a, b):
     print("Dividing %d / %d " %(a, b))
     return a / b
     
def divby2(a):
    print("printing if a is divisble by 2 or not")
    if (a % 2 == 0):
    print(" a is divisble by 2")
    else
    print("a is not divisble by 2")
    
 print(divby2(4))   
    
print("Lets do some math with just functions!")
 
age = add(30,5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
 
print("Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq))
 
 # Apuzzle for the extra credit, tyoe it in anyway
print("Here is a puzzle")
 
what = subtract(age,add(height, multiply(weight,divide(iq, 2))))
 
print("That becomes:", what, "Can you do it by hand?")
