# defines the function cheese_and_crackers with the arguments cheese_count
# and boxes_of_crackers. prints strings containing room for numbers of things
import random
import sys
from sys import argv
from os.path import exists

script, filename1, filename2, filename3 = argv

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

def my_own_function(number_of_pizzas, servings_of_fries, f=sys.stdout):
    f.write("There are %r Pizzas.\n" % number_of_pizzas)
    f.write("There are %r servings of fries.\n\n" % servings_of_fries)

def my_second_function():
    my_own_function(700, 400)

my_own_function(20,30)
my_own_function("two", "three")

pizzas = 50
fries = 60
my_own_function(pizzas, fries)
my_own_function(20 / 2, 3 * 5)
my_own_function(pizzas + 1, fries + 10)

pizzas2 = float(raw_input("Enter number of pizzas!"))
fries2 = float(raw_input("Enter amount of fries!"))
my_own_function(pizzas2, fries2)

content1 = float(open(filename1).read())
content2 = float(open(filename2).read())
my_own_function(content1, content2)

pizzas3 = random.choice([1, 2, 3, 4, 5])
fries3 = random.choice([1, 2, 3, 4, 5])
my_own_function(pizzas3, fries3)

my_second_function()
f = open(filename3, "w")
my_own_function(33, 44, f)









# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
