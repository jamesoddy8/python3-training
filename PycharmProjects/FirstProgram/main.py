print("Hello World")

print(int("5") + int("7"))

# TYPES

# how to convert string to integer - wrap it in int(" ")

# convert text to integer doesn't work - int("hello") will throw an error

# for strings where you need to include "", wrap in single ' quotes - 'She said "I want this"'
# 'She said "Don't put that there"' will throw an error

# 'She said "Don\'t Do That"'
# What "\" does is tells the interpreter to read the following character as a string - so "don\'t" would return "don't"

# STRINGS & INTEGERS

print('She said "Don\'t Do That"')

print("H" + "e" + "l" + "l" + "o")

print("This costs " + str(6) + " dollars")

print("This costs " + str(5+9) + " dollars")

print("Hello:James:Amazing".split(":"))

print("My name is " + "Hello:James:Amazing".split(":")[1])

# BOOLEANS

# True and False are case sensitive

# == comparing to check if two numbers are equal to each other
# 5 == 5 will equal True
# 5 == 4 will equal False

print(5 == 5)
print(5 == 4)

# You can also do comparisons using "is" and "is not" but only in the python3 console

# Lists aka Arrays
# defining an array
# open a close []

print("I like " + ["Movies", "Games", "Python"][2])


# Dictionaries