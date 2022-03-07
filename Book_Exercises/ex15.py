from sys import argv #import arguments from sys or giving arguments as inputs from system

script, filename = argv # arguments name

txt = open(filename) #opening text file named ex15_sample.txt

print("Here's your file %r:" % filename) #printing
print(txt.read()) #printing text of file

print("Type the filename again:")
file_again = input(">") # giving filename in input function

txt_again = open(file_again) # opening the file above mentioned

print(txt_again.read()) # reading and printing file content
 