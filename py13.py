# imports a module
# argv is the argument variable. It holds arguments that are passed to the script
from sys import argv

# unpacks the argv: argv is assigned to four variables
script, first, second, third, fourth = argv
print "What is your argument?"
fifth = raw_input()
# script calls up the name of the file, the other arguments have to be added
# after the filename. If the wrong number of arguments is provided, the argv
# won't unpack
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "This is the end:", fourth
print "This is your argument: %r " % fifth


# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
