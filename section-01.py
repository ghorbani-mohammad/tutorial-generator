# initial example, normal function

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

infinite = infinite_sequence()
print(type(infinite))
print(next(infinite))
print(next(infinite))

# Output:
#    <class 'generator'>
#    0
#    1


# Now we want to add another yield to it
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        yield "This is the second yield statement!"