# Two examples are in this file:
# 01: Infinite counter
# 02: Example with having two yield


# 01: Infinite counter


def infinite_sequence():
    num = 0
    while True:
        return num
        num += 1


# Converting above function to a generator
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


# infinite = infinite_sequence()
# print(type(infinite))
# print(next(infinite))
# print(next(infinite))

# Output:
#    <class 'generator'>
#    0
#    1


# 02: Example with having two yield
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        yield "This is the second yield statement!"


# infinite = infinite_sequence()
# print(type(infinite))
# print(next(infinite))
# print(next(infinite))
# print(next(infinite))

# Output:
#    <class 'generator'>
#    0
#    This is the second yield statement!
#    1
