people = 30
cars = 40
trucks = 15

# if splits the code into more then one way to continue the code.
if cars > people:
# prints the string, if condition is true
    print "We should take the cars."
# if the first condition is false, elif provides a second condition.
elif cars < people:
# prints the string, if condition is true
    print "We should not take the cars."
# if the first and second condition are false, else is processed.
else:
# prints the string, if above conditions are false
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks"
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks and cars < trucks:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay at home then."


# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
