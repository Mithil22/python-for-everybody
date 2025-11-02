# Python Syntax Quick Reference

## Variables and Data Types

```python
# Integer
age = 25

# Float
height = 5.9

# String
name = "John"

# Boolean
is_active = True

# Multiple assignment
x, y, z = 1, 2, 3
```

## Operators

```python
# Arithmetic
+ - * / // % **

# Comparison
== != > < >= <=

# Logical
and or not

# Membership
in not in
```

## String Operations

```python
# Concatenation
full_name = first + " " + last

# F-strings (formatted strings)
message = f"Hello {name}, you are {age} years old"

# Common methods
text.upper()
text.lower()
text.strip()
text.split()
text.replace("old", "new")
```

## Control Flow

```python
# If statement
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# For loop
for item in sequence:
    # code

# While loop
while condition:
    # code
```

## Functions

```python
# Define a function
def function_name(parameter1, parameter2):
    # code
    return result

# Call a function
result = function_name(arg1, arg2)
```

## Lists

```python
# Create a list
numbers = [1, 2, 3, 4, 5]

# Access elements
first = numbers[0]
last = numbers[-1]

# Common operations
numbers.append(6)
numbers.remove(3)
len(numbers)
numbers.sort()
```

## Dictionaries

```python
# Create a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Access values
name = person["name"]
age = person.get("age")

# Add/modify
person["email"] = "john@example.com"
```

## File Operations

```python
# Read file
with open("file.txt", "r") as file:
    content = file.read()

# Write file
with open("file.txt", "w") as file:
    file.write("Hello, World!")
```

## Common Built-in Functions

```python
print()      # Output to console
input()      # Get user input
len()        # Length of sequence
type()       # Get type of object
int()        # Convert to integer
float()      # Convert to float
str()        # Convert to string
range()      # Generate sequence of numbers
sorted()     # Return sorted list
sum()        # Sum of numbers
max()        # Maximum value
min()        # Minimum value
```

## Tips for Data Engineering

```python
# Reading CSV files (you'll use this a lot!)
import pandas as pd
df = pd.read_csv("data.csv")

# List comprehension (powerful and common)
squares = [x**2 for x in range(10)]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(10)}

# Lambda functions (anonymous functions)
double = lambda x: x * 2
```
