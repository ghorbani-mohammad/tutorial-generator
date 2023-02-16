# Generator by comprehension
# Notice that in Python, using parenthesis (expression) is a generator
# Look at below example, squared is a generator
# Notice that you can use generator in for loops without next

squared = (x**2 for x in range(5))
for num in squared:
    print(num)

# Output:
#    0
#    1
#    4
#    9
#    16
