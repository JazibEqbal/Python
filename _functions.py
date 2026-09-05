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


def positional_only_argument(a, b, /, c, d):
    print(a, b, c, d)

positional_only_argument(3, 4, 5, d=6) # allowed i.e., every argument before / must be positional only. '/'  cannot be the 1st argument as by default all args are keyword-positional only. Hence, it does not make sense.


def keyword_only_argument(a, b, *, c, d):
    print(a, b, c, d)

keyword_only_argument(3, 4, c=5, d=6) # allowed i.e., every argument after * must be keyword only. '*'  cannot be the last argument as by default all args are keyword-positional only. Hence, it does not make sense.


def variable_length_positional_argument(a, b, *args):
    print(a, b, args)

variable_length_positional_argument(1, 2, 3, 4, 5) # before *args all arguments must be positional only, and after it must be keyword only.


def variable_length_keyword_argument(a, b, **kwargs):
    print(a, b, kwargs)

variable_length_keyword_argument(1, 2, c=3, d=4, e=5) # arguments cannot follow var-keyword argument


def factorial_of_a_number_using_recursion(n):
    if n == 1:
        return 1
    else:
        return n * factorial_of_a_number_using_recursion(n - 1)

print(factorial_of_a_number_using_recursion(5))


# 1st class function, function as an object
def fun():
    print("hello")

f = fun
f()

show = print
show("hello")


# Function as a parameter
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def arithmetic(f, x, y):
    return f(x, y)

sum = arithmetic(add, 10, 5)
sub = arithmetic(subtract, 10, 5)
print(sum)
print(sub)