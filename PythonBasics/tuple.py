# Creating Tuples
# Tuples are defined using parentheses (), or simply by separating values with commas.

# Examples:
# Basic tuple

my_tuple = (1, 2, 3, "hello", 4.5)

# Tuple without parentheses (valid)

another_tuple = 1, 2, 3  

# Single-element tuple (comma needed)

single_element_tuple = (5,)  

print(type(single_element_tuple))  # Output: <class 'tuple'>

# Accessing Tuple Elements
# Tuples use zero-based indexing like lists.
  
my_tuple = ("apple", "banana", "cherry")

print(my_tuple[0])  # Output: apple
print(my_tuple[-1]) # Output: cherry (negative indexing)

# Slicing Tuples
# Tuples support slicing to extract parts of them.

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])  # Output: (20, 30, 40)
print(numbers[:3])   # Output: (10, 20, 30)
print(numbers[::2])  # Output: (10, 30, 50) (step of 2)

# Tuple Immutability
# Tuples cannot be modified after creation.

my_tuple = (1, 2, 3)
my_tuple[1] = 10  #error itakua hapa

# Tuple Packing & Unpacking
# Tuples support packing (grouping values) and unpacking (extracting values).

# Packing
person = ("John", 30, "Engineer")

# Unpacking
name, age, job = person
print(name)  # Output: John
print(age)   # Output: 30
print(job)   # Output: Engineer

# When to Use Tuples?
#✅ When data should not be modified.
#✅ When using dictionary keys (tuples are hashable).
#✅ When returning multiple values from a function.

def get_coordinates():
    return (10.5, 20.8)

x, y = get_coordinates()
print(x, y)  # Output: 10.5 20.8
