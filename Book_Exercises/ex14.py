from sys import argv
script, user_name, dislikes = argv
prompt = '> '

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("you dislike %s in me" % dislikes)
dislike=input()

print("Where do you live %s" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
ALright, so you said %r about liking me.
You live in %r. Not sure where that is.
ANd you have a %r computer. Nice.
""" % (likes, lives, computer))