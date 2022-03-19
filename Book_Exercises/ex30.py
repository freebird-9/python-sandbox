people = 30
cars = 40
buses = 5

if cars > people and buses == cars:
    print("We should take the cars.")
elif cars < people:
     print("We should not take the cars.")
else:
    print("We cant decide.")
    
if buses > cars or people != cars:
    print("That's too many buses.")
elif buses < cars:
    print("May be we could take buses.")
else:
    print("We still cant decide. ")
    
if people > buses:
    print("Alright, lets just take the buses.")
else:
    print("Fine, let's stay homw then.")