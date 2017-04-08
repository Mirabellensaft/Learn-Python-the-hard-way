# this one is like your scripts with argv
# defines a function with the name print_two
def print_two(*args):
# two arguments inside the parameter *args
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do things
# same as print_two, except without unpacking arguments
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

# call the function
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
