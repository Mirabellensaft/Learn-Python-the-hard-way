#Defines the variable formatter as formatted strings
formatter = "%r %r %r %r"

#prints the variable, with different Things replacing the formatter
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing",
    "That you could type right.",
    "But it didn't sing.",
    "So I said goodnight."
)

#Mistakes I make:
#Typos
#forgot quotes
#forgot formatter %
