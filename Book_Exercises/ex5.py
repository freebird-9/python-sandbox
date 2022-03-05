# -- coding: utf-8 --
my_name = 'Shalu'
my_age = 22  # forever
my_height = 5  # feet
my_weight = 45  # kg
my_teeth = 'White'
my_eyes = 'Blue'
my_hair = 'Black'

print("Lets talk about %s." % my_name)
print("She's %d feet tall." % my_height)
print("She's %d kgs heavy." % my_weight)
print("Actually thats not too heavy.")
print("She's got %s eyes and %s hair." % (my_eyes, my_hair))
print("Her teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_weight))