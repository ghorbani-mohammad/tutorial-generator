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
