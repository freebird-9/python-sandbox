MyDict = {
    "fast" : "In aquick Manner",
    "Harry" : "A loner",
    "marks" : [1,2,3],
    "anotherdict" : {'harry': 'player'},
    1:2
}

#Dictionary methods
# print(list(MyDict.keys())) #print the keys of the dictionary
# print(MyDict.keys()) #print the values of the dictionary
# print(MyDict.items())

anotherdict = {
    "lol" : "lollol",
    "Shalu" : "Kumari"
}

MyDict.update(anotherdict)
# print(MyDict)

#difference between .get and [] methods
print(MyDict.get("Harry2")) #returns None as harry2 is not presnet in the dictionary
print(MyDict["Harry2"]) #throws error as harry2 is not present in the dictionary