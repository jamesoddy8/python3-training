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


# Default arguments

def print_something(name, age):
    # print("My name is " + name + " and my age is " + str(age))
    print("My name is", name, "and my age is", age)


# There is no need to use "+" to concatenate, using a "," works as well.


print_something("James", 29)


def print_something_again(name="Someone", age="Unknown"):
    print("My name is", name, "and my age is", age)


print_something_again("Yuki", 25)

print_something_again(None, 27)


def print_people(*people):
    for person in people:
        print("This person is", person)


print_people("James", "Matthew", "Joseph", "William", "Denise")


# asterisk tells this argument that it will be an array of all the arguments that are passed into the function


def do_math(num1, num2):
    return num1 + num2


math1 = do_math(5, 7)
math2 = do_math(11, 34)

print("first sum is", math1, "and the second sum is", math2)

# if / else statements


check = "Lobster"

if check == False:
    print("It is false")
elif check == "Lobster":
    print("Yum, Lobster!!")
elif check == "Yo":
    print("Hello")
else:
    print("It is actually equal to true")

# for / while loops
# for loops

numbers = [1, 2, 3, 4, 5]
people = ["James", "Matthew", "Joseph", "William", "Denise"]

for item in numbers:
    print(item)
for item in people:
    print(item)

# while loop

run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1

# regex

# > re.sub('', '', string)


# three parameters that this sub function takes is the matches we want to make, what we want to replace them with and
# then the string we want to manipulate

# rules in regex are contained within square brackets re.sub('[A, B, C]', '', string)


# >>> import re
# >>> string = "We love to dance! We love to laugh!"
# >>> print(string)
# >>> We love to dance! We love to laugh!
# >>> new = re.sub('[A-Z]', '', string)
# >>> print(new)
# >>> e love to dance! e love to laugh!

# >>> new = re.sub('[a-z]', '', string)
# >>> print(new)
# >>> W   ! W   !


# in rules \ is used to escape the quote
# >>> new = re.sub('[.!,\']', '', string)
# >>> print(new)
# >>> We love to dance We love to laugh

# you can combine these [.,\'a-zA-Z] to remove all the letters (but not the spaces)

# for spaces you use +" " within the rules so...
# new = re.sub('[" "]', '', string) or [a-z+" "]
# print(new)
# Welovetodance!Welovetolaugh!

# if you want to do this for a string with numbers included...

# >>> print(string)
# We love to dance! We love to laugh!37 - 678
# >>> new = re.sub('[^0-9]', '', string)
# >>> print(new)
# >>> 37678