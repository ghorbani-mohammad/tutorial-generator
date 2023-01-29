# Another example of generators using itertools module

import itertools

squared = (x**2 for x in itertools.count(start=0, step=2))
for num in itertools.islice(squared, 5):
    print(num)


# Output:
#    0
#    4
#    16
#    36
#    64
