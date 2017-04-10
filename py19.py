# defines the function cheese_and_crackers with the arguments cheese_count
# and boxes_of_crackers. prints strings containing room for numbers of things
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# calls the function, assigning numbers to the arguments.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# calls the function, using the arguments as variables and assigning them
# numbers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# calls the function, assigning variables to the arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# calls the function assigning math operations to variables
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# calls the function, adding numbers to the variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
