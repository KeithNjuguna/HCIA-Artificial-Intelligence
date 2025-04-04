#Lists.
#1.Lists
#Mutable (can be changed after creation).
#Defined using square brackets [].
#Can store different data types.
#upports indexing, slicing, and various list methods.

my_list = [1, 2, 3, "hello", 4.5]
my_list.append(6)  # Adds an element
my_list[1] = 10    # Modifies an element
print(my_list)  # Output: [1, 10, 3, 'hello', 4.5, 6]

# Function	Description:
# len(list)	Returns the number of elements.
# sum(list)	Returns the sum of all numeric elements.
# max(list)	Returns the largest element.
# min(list)	Returns the smallest element.
# sorted(list)	Returns a sorted copy of the list.
# list()	Converts an iterable (like a tuple) to a list.
# any(list)	Returns True if any element is True.
# all(list)	Returns True if all elements are True.

# Method	Description:
# append(x)	Adds x to the end of the list.
# extend(iterable)	Adds multiple elements from an iterable.
# insert(i, x)	Inserts x at index i.
# remove(x)	Removes the first occurrence of x.
# pop(i)	Removes and returns the element at index i.
# index(x)	Returns the index of the first occurrence of x.
# count(x)	Returns the number of times x appears.
# sort()	Sorts the list in ascending order.
# reverse()	Reverses the order of elements.
# copy()	Returns a shallow copy of the list.
# clear()	Removes all elements from the list.

# Example of Methods in use;
my_list = [3, 1, 4, 1, 5]
my_list.append(9)  # [3, 1, 4, 1, 5, 9]
my_list.sort()     # [1, 1, 3, 4, 5, 9]
print(my_list.count(1))  # Output: 2
# Example of Functions in use;
numbers = [4, 2, 9, 1]
print(len(numbers))  # Output: 4
print(sum(numbers))  # Output: 16
print(max(numbers))  # Output: 9
print(sorted(numbers))  # Output: [1, 2, 4, 9]



