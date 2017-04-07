# imports a module
from sys import argv

# unpacks the container
script, filename = argv

# opens a file with the filename provided
# it takes a parameter and returns a value that is set as a variable (txt)
txt = open(filename)

# prints the content of the file with a header
print "Here's your file %r:" % filename
# calls a function on txt named read
print txt.read()

# a different way of opening a file when script is already running
print "Type the filename again:"
# asks for a raw_input that is defined as a variable
file_again = raw_input(">")
# the parameter file_again is opened and returns a value that is set as another variable
txt_again = open(file_again)
# the function .read is called on the variable that is defined earlier
print txt_again.read()

txt.close()
txt_again.close()


# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
