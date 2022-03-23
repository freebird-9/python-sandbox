# def celtofah(cal):
/rint("Fahrenheit is equal to " +  str(f))

#prob3 how to prevent python to print new line
print("Hello ", end= "")
print("How ", end ="")
print("are ", end="")
print("you ", end="")
# by default its \n add end= "" in print

#prob4 funtion to print sum of n naturals number
def sum(n):
    sum =0
    for i in range(1,n+1):
        sum= sum+i
        i = i+1
    return sum
s = sum(500)
print("Sum of n natural numbers is equals to " + str(s))

# def sumrecur(n):
    if n == 1:
        return 1
    else:
        sum = sumrecur(n-1) + n
    return sum

# s = sumrecur(4)
# print("sum", str(s))

#print star
n= 3
for i in range(n):
    print(" * " * (n-i))

#inche sto cms
def inchtocms(inch):
    cms = inch*2.54
    return cms
c = inchtocms(4)
print("cm value is equal to" +str(c))

def rem(word):
    list = ["apple", "oranges", "kiwi", "grapes"]
    list.remove(word)
    return list

c = rem("apple")
print(c)


