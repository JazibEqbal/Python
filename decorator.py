# A decorator functions takes a function as a parameter, access outer function, and returns inner function.
# modifies the function

def outer(f):
    def inner():
        print("+" * 10)
        f()
        print("+" * 10)
    return inner

@outer
def display():
    print("welcome")

# display = outer(display)
display()