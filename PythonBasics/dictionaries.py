# Dictionaries in Python 
# A dictionary is an unordered, mutable collection of key-value pairs. It’s one of Python’s most powerful data structures and is written using curly braces {}.
# Creating a Dictionary
my_dict = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
Keys: "name", "age", "is_student"

Values: "Alice", 25, True

# Accessing Values

print(my_dict["name"])       # Output: Alice
print(my_dict.get("age"))    # Output: 25
Use [] or .get() to retrieve a value by key.

.get() won’t throw an error if the key doesn’t exist (returns None instead).
                                                      
# Adding and Updating Items
                                                      
my_dict["city"] = "Nairobi"     # Add new key-value
my_dict["age"] = 26             # Update existing key


# Removing Items

my_dict.pop("age")         # Removes key 'age'
del my_dict["is_student"]  # Also removes key
my_dict.clear()            # Empties the entire dictionary

# Dictionary Methods
# Method	Description
# .get(key)	Gets value for key, or None if not found
# .keys()	Returns all keys
# .values()	Returns all values
# .items()	Returns all key-value pairs
# .pop(key)	Removes key and returns its value
# .update(dict2)	Updates with another dictionary
# .clear()	Empties the dictionary

info = {"name": "Bob", "age": 30}
print(info.keys())    # dict_keys(['name', 'age'])
print(info.values())  # dict_values(['Bob', 30])

# Nesting Dictionaries 

student = {
    "name": "Eve",
    "grades": {"math": 90, "science": 88}
}
print(student["grades"]["math"])  # Output: 90
