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

print("This costs " + str(5 + 9) + " dollars")

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

# Curly braces - use to define a dictionary
print({"name": "James", "age": "29", "hobby": "code"}["name"])

# Variables

greeting = "Hello World"
print(greeting)

greeting = greeting.split(" ")[0]
print(greeting)

# convert to string str()
str(4)
str(4.6)
str(True)

# convert to integer int() and then float() for floats or bool("True") for booleans
print(int("4"))
print(float("2.5"))
print(bool("True"))

# len() used to determine length of something e.g. len("Hello") = 5 or len(1, 2, 3, 4) = 4

# sorted(5,4,3,2,1) = (1,2,3,4,5) sorted("J","A","M","E","S")
# sorting puts numbers first, then capital alphabet and then lowercase
print(sorted(["J", "A", "M", "E", "S"]))


# start two lines down
# CamelCase is used in python for class names MyClass
# snake_case (separating words with underscores) is used for functions e.g. my_function()

# starting a function
#
# def my_function():
#     print("This is my function!")
#     print("This is the second string.")
#
#
# my_function()


def my_function(str1, str2, str3, str4):
    print(str1)
    print(str2)
    print(str3)
    print(str4)

my_function("'But I don't want to go among mad people,' Alice remarked.",
            "'Oh, you can't help that,' said the Cat: 'we're all mad here. I'm mad. You're mad.'",
            "'How do you know I'm mad?' said Alice.",
            "'You must be,' said the Cat, 'or you wouldn't have come here.")
