def _iterator(l):
    it = iter(l) # iter creates an iterator object
    print(next(it)) # with next() it prints and mobes to next item
    print(next(it))
    print(next(it))

_iterator(l=[1, 2, 3])


def _generators(d):
    i = 0
    while True:
        yield d[i]
        i =  (i + 1) % len(d)

days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']

day = _generators(days) # generator object
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))
print(next(day))


def fibonacci_using_generator(n):
    a, b = 0, 1
    for i in range(n + 1):
        yield a
        a, b = b, a + b

for term in fibonacci_using_generator(10):
    print(term)
