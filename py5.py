name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # Ibs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height2 = height * 2.5 #cm
weight2 = weight * 0.453592 #kg

print "Let's talk about %s." % name
print "He's %d inches tall. This equals %d cm." % (height, height2)
print "He's %d pounds heavy. This equals %d kg." % (weight, weight2)
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His theeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
