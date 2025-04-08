1. Conditional Statements:

Conditional statements allow your Python program to make decisions and execute different blocks of code based on whether certain conditions are true or false.

if statement: Executes a block of code only if a specified condition is true.

Python

x = 10
if x > 5:
    print("x is greater than 5")
elif statement: Allows you to check multiple conditions in sequence. It's executed only if the preceding if or elif condition was false and the current elif condition is true. You can have multiple elif statements.

Python

grade = 75
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("Below C")
else statement: Specifies a block of code to be executed if all preceding if and elif conditions are false. You can have at most one else statement in an if-elif-...-else block, and it must be the last one.

Python

number = -3
if number > 0:
    print("Number is positive")
else:
    print("Number is not positive (could be zero or negative)")
2. Looping Statements:

Looping statements allow you to repeat a block of code multiple times. Python provides two main types of loops: for loops and while loops.

for loop: Iterates over a sequence (like a list, tuple, string) or other iterable objects.

    fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
print(fruit)
```

You can also use the `range()` function with `for` loops to iterate a specific number of times:

```python
for i in range(3):  # Iterates from 0 to 2
    print(f"Iteration number: {i}")
```
while loop: Executes a block of code as long as a specified condition is true. You need to be careful with while loops to ensure that the condition eventually becomes false to avoid an infinite loop.

Python

count = 0
while count < 5:
    print(f"Count is: {count}")
    count += 1
3. Control Flow within Loops:

Python provides break and continue statements to control the flow of execution within loops.

break statement: Immediately terminates the loop and the program control flows to the statement immediately following the loop.

Python

numbers = [1, 2, 3, 4, 5, 6]
target = 4
for num in numbers:
    print(f"Checking: {num}")
    if num == target:
        print(f"Found the target: {target}")
        break  # Exit the loop
