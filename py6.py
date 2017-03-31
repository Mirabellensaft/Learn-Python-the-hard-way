# the variable x is a string containing a formated string
x = "There are %d types of people." % 10
# the variable binary is the string "binary"
binary = "binary"
# the variable do_not is the string "binary"
do_not = "don't"
# the variable y is a string containing two formated strings, containing the variables binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)
# prints the variable x
print x
# prints the variable y
print y
# prints a string containing formated string, insterting variable x
print "I said: %r." % x
# prints a string containing a formated string, insterting variable y
print "I also said: '%s'." % y
# the variable hilarious is False
hilarious = False
# the variable joke_evluation is a string with a formated string attached
joke_evluation = "Isn't that joke so funny?! %r"

# printing the last two variables connected with a formated string brings things together
print joke_evluation % hilarious
# a different way of bringing strings together is to just assign variables to them, and print the addition of them.
w = "This is the left side of..."
e = "a string with a right side."

print w + e
