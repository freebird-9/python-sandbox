# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))
    
 # ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
     print("arg1: %r, arg2: %r" %(arg1, arg2))
     
     # this just takes 1 argument
 def print_one(arg1):
     print("arg1: %r" % arg1)
     
 # this one takes no arguments
 def print_none():
     print("I got nothin' .")
     
 print_two("Shalu", "Kumari")
 print_two_again("Shalu", "Kumari")
 print_one("First")
 print_none()