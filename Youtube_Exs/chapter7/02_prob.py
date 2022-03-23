#prob1 multiplication table of a given number
# num = int(input("Enter number to print multiplication number.\n"))
# for i in range(1,11):
#     print(num * i)
#     i = i+1

#prob2 
# l = ["Harry", "Sohan", "Sachin", "Rahul"]
# for i in l:
#     if(i == "Sohan" or "Sachin"):
#         print("Hello")
# else:
#     print("Name start with other letter than s")

#prob3 prob1 using while loop
# i=1
# while i <= 10:
#     print(i*num)
#     i=i+1

#prob4 finding wether number entered is prime or not
# n = int(input("enter number to check prime or not\n"))
# if n > 1:  
#     for i in range(2, int(n/2 +1)):
#         if(n % i == 0):
#          print("n is not prime number")
#          break
#         else:
#          print("n is prime number")
#          break
         
# else:
#         print("n is not prime number")
        

#prob5 sum of n natural numbers
# i = 1
# n = int(input("enter n\n"))
# sum = 0
# while i <= n:
#     sum = sum + i
#     i = i + 1
# print(sum)

#prob6 factorial of a number
n = int(input("Enter number to find factorial\n"))
fact = 1
if n > 1:
 for i in range(n, 1):
    fact = i*fact
    i = i - 1
print(fact)

