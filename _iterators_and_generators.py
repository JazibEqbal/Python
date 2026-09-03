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
