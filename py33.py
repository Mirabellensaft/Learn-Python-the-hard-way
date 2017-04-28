print "Study Drill"

j = 0
zahlen = []

def addition():
    global j
    print "Am Anfang ist j %d." % j
    zahlen.append(j)
    print "Jetzt die Zahlen: ", zahlen
    j = j + 1
    print "Am Ende ist j is %d" % j

addition()
addition()
addition()
addition()
addition()
addition()

for zahl in zahlen:
    print zahl

# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
