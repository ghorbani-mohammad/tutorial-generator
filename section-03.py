# Generator by comprehension
# Notice that in Python the structure of (expression) is a generator

squared = (x**2 for x in range(5))
for num in squared:
    print(num)

# Output:
#    0
#    1
#    4
#    9
#    16
