from sys import argv
from os.path import exists

script, from_file, to_file = argv

#from_file is an object that is opened, the content that is read
# produces a string variable: in_data, which is written in to the out_file.
# out_file has to be closed, as it is an object.
in_data = open(from_file, "r").read()
out_file = open(to_file, "w")
out_file.write(in_data)

out_file.close()


# Mistakes I make:
# Typos
# forgot quotes
# forgot formatter %
# forgot \n

# things to remember:
# go back to study drills of ex 10
