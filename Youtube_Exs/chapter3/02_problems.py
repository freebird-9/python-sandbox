#prob1
name = "Shalu "
a = input(">")
print(name + a )

# problem :2 
letter = '''Dear  <|Name|>
You are selected

Date: <|DATE|>
'''
# print(letter)
# a = input("Enter your name\n")
# b = input("Enter Date\n")
# letter = letter.replace("<|Name|>", a)
# letter = letter.replace("<|DATE|>", b)
# print(letter)

# problem 3 detecting double spaces in a string
string = " Ok  now I have to detect double space in a string."
double_space = string.count("  ")
ds = string.find("  ")
print(double_space)
print(ds)

#problem 4 replace double space with single space
string2 = string.replace("  ", " ")
print(string2)

# problem5 formatting a letter
letter = " Dear Harry, This python course is nice. Thanks."
letter_formatted = "Dear Harry, \n\tThis python course is nice. \n Thanks!"
print(letter_formatted)