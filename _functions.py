def volume(length, breadth, height):
    print(length, breadth, height)
    return length * breadth * height

v = volume(5, 5, 5) # positional arguments (pass in same order)
print(v)
v = volume(breadth=5, height=5, length=5) # keyword arguments (pass in any order)
print(v)
# v = volume(5, length=5, height=5) # error got multiple values for argument 'length', first value 5 goes in length only
# v = volume(5, breadth=5, 5) # error positional argument follows keyword argument, all positional argument must be on left side of keyword argument


def default_argument(l=[1, 2, 3]):
    l.append(len(l))
    print(l)

# DEFAULT ARGUMENT IS CREATED ONLY ONCE
default_argument()
default_argument()
default_argument(l=[10, 11])
default_argument()