from sys import argv

# requires that you give the name of a file as 2nd argument when running
# the script
script, input_file = argv

# defines the function print_all, with the value f. The function reads f,
def print_all(f):
    print f.read()

# defines the function rewind, with value f. Seek sets the current position
# of the file to the offset. f is a fileobject
def rewind(f):
    f.seek(0)

# defines the function print_a_line, with the values line_count and f.
# It prints the variabels line_count and reads one line of the file.
def print_a_line(line_count, f):
    print line_count, f.readline()

# opens the file and generates the file object current_file
current_file = open(input_file)

print "First let's print the whole file:\n"
#prints the entire content of the fileobject
print_all(current_file)

print "Now let's rewind, kind of like a tape."
#resets the file position to the beginning
rewind(current_file)

print "Let's print three lines:"
# gives the value 1 to the variabele current_line
current_line = 1
# prints line one of the file object, because of the current_line variable
print_a_line(current_line, current_file)
# adds + one to the old variable and makes it a new one, so after the addition
# its 2!
current_line += 1
print_a_line(current_line, current_file)
#adds anoter. n= n+1 !
current_line += 1
print_a_line(current_line, current_file)

# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
