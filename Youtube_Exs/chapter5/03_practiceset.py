#problem1 craete hindi dict where user enter hindi word and return english translation of that word

HindiDict = {
    "Kaam" : "Work",
    "sona" : "Sleep",
    "Khana" : "Eat",
    "Ghumna" : "Travel",
    "Naachna" : "Dance"
}

a = input("Enter the hindi word\n")
print("The meaning of word entered by user is", HindiDict.get("a"))
print("The meaning of word entered by user is", HindiDict["a"])

#problem2
a = set() #creating empty set
a1 = int(input("Enter input 1\n"))
a1 = int(input("Enter input 1\n"))
a2 = int(input("Enter input 2\n"))
a3 = int(input("Enter input 3\n"))
a4 = int(input("Enter input 4\n"))
a5 = int(input("Enter input 5\n"))
a6 = int(input("Enter input 6\n"))
a7 = int(input("Enter input 7\n"))
a8 = int(input("Enter input 8\n"))
a.add(a1)
a.add(a2)
a.add(a3)
a.add(a4)
a.add(a5)
a.add(a6)
a.add(a7)
a.add(a8)
print(a)

#prob3
# set = {18, "18"}
# print(set)

#prob4
s = set()
s.add(20)
s.add(20.2)
s.add("20")
# print(len(s))
# print(s)

#prob5
dict = {}
lang1 = input("enter your lang\n")
lang2 = input("enter your lang\n")
lang3 = input("enter your lang\n")
lang4 = input("enter your lang\n")
dict = {
    "Shalu" : lang1,
    "Bhaska" : lang2,
    "Jyoti" : lang3,
    "Abhi" :lang4
} 
print(dict)

#prom9
s = {8,7,12, "Harry",[1,2]}
print(s)