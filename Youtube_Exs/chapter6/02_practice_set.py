num1 = int(input("enter number 1"))
num2 = int(input("enter number 2"))
num3 = int(input("enter number 3"))
num4 = int(input("enter number 4"))

if(num1>num4 and num1>num2 and num1>num3):
    print("num1 is greatest number")
elif(num2>num4 and num2>num1 and num2>num3):
    print("num2 is greatest number")
elif(num3>num4 and num3>num2 and num3>num1):
    print("num3 is greatest")
elif(num4>num1 and num4>num2 and num4>num3):
    print("num4 is greatest")
else:
    print("Its not working")