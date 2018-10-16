# https://realpython.com/primer-on-python-decorators/

# Simple decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hi():
    print("Hi!")

say_hi = my_decorator(say_hi)       # reassign to wrapped function
say_hi()
print()

# Behaviour of decorator depends on time of day
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 20:
            func()
        else:
            pass
    return wrapper

def say_hi():
    print("Hi!")

say_hi = not_during_the_night(say_hi)
say_hi()

# Syntactic Sugar!
@my_decorator
def say_hi2():
    print("Hi!")
say_hi2()

# Decorating Functions With Arguments
def do_twice(func):
    def wrapper(*args, **kwargs):   # wrapper accepts any positional and keyword arguments
        func(*args, **kwargs)       # and passes those arguments to func
        func(*args, **kwargs)
    return wrapper

@do_twice
def say_name(name):
    print(name)

say_name("Jake")

# Returning Values From Decorated Functions
def do_again(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)    # wrapper now returns the return value of func
    return wrapper

@do_again
def say_animal(animal):
    print(animal)
    return animal + " has been decorated."

dec = say_animal("Bat")
print(dec, "\n")

# Introspection - the ability for an object to know about its own attributes at runtime
print(say_animal)
print(say_animal.__name__)  # now "wrapper"

import functools            # to fix the wrong name
def do_again(func):
    @functools.wraps(func)  # decorate the wrapper function
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)    # wrapper now returns the return value of func
    return wrapper

@do_again
def say_name(name):
    print(name)

print(say_name.__name__)    # now correctly "say_name"

# Generic decorator template
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


# Passing arguments to decorators - wrap the decorator in another function
def repeat(num_times):                  # decorator factory
    def decorator_repeat(func):         # the decorator
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):  # argument to decorator factory is used by the wrapper
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=3)
def print_me(text):
    print(text)

print_me("How many times?")

# Decorating methods of classes
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):    # using setter allows error checking
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):         # immutable because there is no @area.setter
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod            # takes the class as argument, not an instance of the class
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod           # a regular function, does not have self argument
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535

# Stateful Decorators

import functools

def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

@count_calls
def say_whee():
    print("Whee!")

print(say_whee())