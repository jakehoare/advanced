
print("############# Frozenset amended")
a = frozenset("abcdef")
try:
    a.update("hello")   # update() is equivalent to |= (i.e. union) except takes any iterator
except Exception as ex:
    print("Methods that mutate frozenset cause", ex.__class__.__name__)

print(id(a))
a |= set("hello")   # a =| s is equivalent to a = a | s, creates a new object a
print(id(a))

b, c = frozenset("defg"), frozenset("ghhi")
d = {a, b, c}       # frozenset is immutable so can be dictionary key or member of set
print(d, "\n")

print("############# Late binding")
def create_multipliers():
    multipliers = []

    for i in range(5):
        def multiplier(x):  # value of i is looked up at the time multiplier() is called
            return i * x    # hence i == 4 for every multiplier
        multipliers.append(multiplier)

    return multipliers

muls = create_multipliers()
for mul in muls:
    print(mul(10))      # prints 40 for all 5 multipliers
print()

print("############# Mutable elements of immutable collections can be updated")
my_tuple = (1, 5, "g", [3, 6])
my_tuple[3].append(9)
print(my_tuple)
print()

print("############# String split produces empty strings for duplicates and ends")
test = "   spaces   abound "
print(test.split(" "))      # 3 leading spaces, one intermediate space, one trailing space
print()

print("############# List without comma separator")
print(["hello" "world", ] == ["helloworld"])    # strings concatenated without comma, trailing comma ignores
print()

print("############# Invert dictionary")
d = {k : v for k, v in zip(range(5), "abcde")}
print(d)
print(dict(zip(d.values(), d.keys())))      # constructor takes tuples from zip
print({v : k for k, v in d.items()})        # invert by comprehension
print()

print("############# Zip to transpose matrix")
mat = [[i for i in range(4)] for _ in range(3)]
print(mat)
print(list(zip(*mat)))  # unpack one element from each row the rows into tuples
print()

print("############# namedtuple")
from collections import namedtuple
Car = namedtuple('Car', ['color', 'mileage'])   # acts like a class without methods and using less memory.
my_car = Car('red', 3812.4)                     # used to return multiple values. Immutable.
print(my_car)
print(my_car.color)
print()

print("############# Print end and flush")
test = [i for i in range(5)]
for item in test:
    print(test)         # prints on separate lines, default end is newline
for item in test:
    print(test, end=", ", flush=True) # prints comma delimited, flushes buffer to print immediately
print()

print("############# Separator for large numbers")
a = 1_000_000       # underscore improves legibility
print(a)
print()
