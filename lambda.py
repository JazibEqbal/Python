# anonymous, single line function

print((lambda x: x**2)(5))

# filter
l1 = [1,2,3,4,5,6]
f = filter(lambda x: x % 2 == 0, l1)

print(list(f))

# map
m = map(lambda x: x + 1, l1)
print(list(m))

print(list(map(lambda x: x if x % 2 == 0 else -x, l1)))
