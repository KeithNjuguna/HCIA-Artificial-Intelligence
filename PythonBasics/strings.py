# Definition of a String
# In Python, a string is a sequence of characters (letters, numbers, symbols) enclosed within single quotes (') or double quotes ("). Strings are immutable, meaning once created, their contents cannot be changed. Examples:

text = "Hello, Python!"
name = 'Alice'

# String Formatting (1)
# String formatting refers to creating formatted strings by embedding variables or expressions. Python offers multiple ways to format strings:

# f-strings (formatted string literals): Introduced in Python 3.6, they allow you to embed expressions directly within curly braces {}.

name = "Alice"
print(f"Hello, {name}!")  # Output: Hello, Alice!
format() method: Uses placeholders ({}) for substituting values.

age = 25
print("Alice is {} years old.".format(age))  # Output: Alice is 25 years old.
Old-style formatting: Uses % for substitution (less commonly used now).

print("The value is %d" % 10)  # Output: The value is 10
String Operators
Python provides several operators for manipulating strings:

Concatenation (+): Combines two strings into one.

greeting = "Hello" + " World"  # Output: Hello World
Repetition (*): Repeats a string multiple times.

repeat = "Hi! " * 3  # Output: Hi! Hi! Hi!
Membership (in): Checks if a substring exists within a string.

print("Py" in "Python")  # Output: True
Comparison (==, <, >): Compares two strings lexicographically.

print("apple" < "banana")  # Output: True
# String Methods
# String methods are built-in functions associated with strings. They allow for manipulation and transformation. Examples:

lower(): Converts the string to lowercase.

upper(): Converts the string to uppercase.

strip(): Removes whitespace from the start and end.

split(): Splits the string into a list based on a delimiter.

join(): Joins a list of strings into a single string with a delimiter.

replace(): Replaces occurrences of a substring with another.

find(): Searches for a substring and returns its index.

Example:

text = " Hello, Python! "
print(text.strip().replace("Python", "World").upper()) 

# String Modules
# Python has specific modules for advanced string operations:

string module: Provides constants and tools for working with strings.

import string
print(string.ascii_letters)  # Output: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)         # Output: 0123456789
re module: Enables operations with regular expressions for pattern matching in strings.

import re
result = re.search(r'\d+', "Age: 25")
print(result.group())  # Output: 25
