from sys import argv

script, user_name, age = argv
promt = "--->"

print "Hi %s, I'm the %s script." % (user_name, script)
print "You are %s years old." % age
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(promt)

print "Where do you live %s?" % user_name
lives = raw_input(promt)

print "What kind of computer do you have?"
computer = raw_input(promt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
