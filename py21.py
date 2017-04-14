def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" %(a, b)
    return a - b

def multipy(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multipy(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq)


# A puzzle for the extra credit, type in anyway.

print "Here is a puzzle."

what = add(age, subtract(height, multipy(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

print "Sure, let me show you!"

solution = ((30 + 5)+((78 - 4)-((90 * 2) * ((100 / 2) / 2))))

print "See how smart I am, look at this", solution, "!"

print "Now I break the formula by deleteing all ():"

solution2 = 30 + 5 + 78 - 4 - 90 * 2 * 100 / 2 / 2

print solution, "is the same as", solution2, ". Because python knows math rules."

solution3 = 30 * 2 + 5 * 100 + 78 / 2 - 4 / 2 - 90

print solution3, "is different, because I changed the order of the terms."

print "Now I will make my own formula into a function."

solution4 = 24.0 + 34.0 / 100.0 - 1023.0

term1 = divide(34.0, 100.0)
term2 = add(24.0, term1)
term3 = subtract(term2, 1023.0)

print term3, "and", solution4


# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
