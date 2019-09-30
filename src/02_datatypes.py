"""
Python is a strongly-typed language under the hood, which means 
that the types of values matter, especially when we're trying
to perform operations on them. 

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12
# Nesting both inside an `int()` to make for a case-agnostic solution
print(int(x) + int(y))

# Write a print statement that combines x + y into the string value 57
# Same as above, creating a solution that will work regardless of one of the two being an int
print(str(x) + str(y))