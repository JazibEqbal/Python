# Python Notes

## 1. Basic Concepts

### Program

A **program** is a set of instructions performed on some data.

### Statically Typed Language

In a statically typed language, the data type of a variable is **declared or determined before runtime**.

```c
int x = 10;
```

### Dynamically Typed Language

In a dynamically typed language, the data type of a variable is **determined at runtime**.

```python
x = 10
```

In Python, you do not explicitly declare the type of a variable. The variable refers to an object, and the object has a type.

---

## 2. Python Characteristics

* Python is **dynamically typed**.
* Python is **case-sensitive**.
* Everything in Python is an **object**.
* Variables in Python are **references to objects**.

### Multiple Variables Referencing the Same Object

For example:

```python
a, b, c = 1, 1, 1
```

Since integers are immutable, Python may reuse the same integer object for the value `1`. Thus, the variables can refer to the same object.

```python
print(id(a))
print(id(b))
print(id(c))
```

However, it is important to note that **Python's object allocation and interning behavior should not be relied upon for program logic**.

Use `==` to compare values and `is` to compare object identity.

```python
a == b   # Value comparison
a is b   # Identity comparison
```

---

# 3. Data Types

| Type       | Ordered | Mutable | Index-Based | Example     |
| ---------- | ------- | ------- | ----------- | ----------- |
| `int`      | —       | No      | —           | `10`        |
| `float`    | —       | No      | —           | `3.14`      |
| `complex`  | —       | No      | —           | `2 + 3j`    |
| `bool`     | —       | No      | —           | `True`      |
| `str`      | Yes     | No      | Yes         | `"Hello"`   |
| `list`     | Yes     | Yes     | Yes         | `[1, 2, 3]` |
| `tuple`    | Yes     | No      | Yes         | `(1, 2, 3)` |
| `set`      | No      | Yes     | No          | `{1, 2, 3}` |
| `dict`     | Yes*    | Yes     | No          | `{"a": 1}`  |
| `NoneType` | —       | No      | —           | `None`      |

> **Note:** Dictionaries preserve insertion order in Python 3.7+, but they are accessed using **keys**, not numerical indexes.

---

# 4. Literals

A **literal** is a fixed value written directly in the source code.

```python
a = 6
```

Here, `6` is an integer literal.

Examples:

```python
10
3.14
"Hello"
True
None
[1, 2, 3]
(1, 2, 3)
```

> **Note:** Literals are not necessarily "created only once." Python may reuse objects through mechanisms such as interning/caching. Do not depend on this behavior.

For example:

```python
x = 25
y = 25
```

Do **not** assume that `x is y` will always be true merely because both values are `25`.

Use:

```python
x == y
```

to compare values.

---

# 5. Operators and Operands

Consider:

```python
x = 5 + 6
```

* `5` and `6` are **operands**.
* `+` is an **operator**.

---

# 6. Short-Circuit Evaluation

When using logical operators such as `and` and `or`, Python may stop evaluating as soon as the final result is known.

This is called **short-circuit evaluation**.

### `and`

If the first condition is `False`, Python does not evaluate the remaining conditions.

```python
False and some_function()
```

The function does not need to be called because the result is already known to be `False`.

### `or`

If the first condition is `True`, Python does not evaluate the remaining conditions.

```python
True or some_function()
```

The function does not need to be called because the result is already known to be `True`.

---

# 7. Bitwise Operators

Bitwise operators work on the binary representation of integers.

## Bitwise AND `&`

If both corresponding bits are `1`, the result is `1`; otherwise, it is `0`.

Example:

```text
10 = 1010
13 = 1101
---------
     1000
```

Therefore:

```python
10 & 13
# 8
```

Binary representation:

```python
format(8, 'b')
# '1000'
```

---

## Bitwise OR `|`

If either corresponding bit is `1`, the result is `1`.

```text
10 = 1010
13 = 1101
---------
     1111
```

Therefore:

```python
10 | 13
# 15
```

```python
format(15, 'b')
# '1111'
```

> **Important:** `!` is **not** Python's bitwise OR operator. Python uses `|` for bitwise OR.

---

# 8. Left Shift

The left-shift operator is:

```python
<<
```

For non-negative integers, shifting left by `n` positions is equivalent to multiplying by `2**n`.

```text
a << n == a * (2 ** n)
```

Example:

```python
a = 10
```

Binary:

```text
10 = 1010
```

### Shift by 1

```python
a << 1
```

```text
1010 << 1 = 10100
```

```text
10100 = 20
```

### Shift by 2

```python
a << 2
```

```text
1010 << 2 = 101000
```

```text
101000 = 40
```

---

# 9. Right Shift

The right-shift operator is:

```python
>>
```

For non-negative integers, shifting right by `n` positions is equivalent to integer division by `2**n`.

```text
a >> n == a // (2 ** n)
```

Example:

```python
a = 10
```

Binary:

```text
10 = 1010
```

### Shift by 1

```python
a >> 1
```

```text
1010 >> 1 = 0101
```

```text
0101 = 5
```

### Shift by 2

```python
a >> 2
```

```text
1010 >> 2 = 0010
```

```text
0010 = 2
```

> **Note:** For negative integers, right-shift behavior is based on Python's signed integer semantics, so the simple division formula should not be treated as a universal rule.

---

# 10. `range()`

Syntax:

```python
range(start, stop, step)
```

| Argument | Optional? | Default |
| -------- | --------- | ------- |
| `start`  | Yes       | `0`     |
| `stop`   | No        | —       |
| `step`   | Yes       | `1`     |

Example:

```python
range(5)
```

Equivalent to:

```python
range(0, 5, 1)
```

Produces:

```text
0, 1, 2, 3, 4
```

> `stop` is **exclusive**.

---

# 11. String

A string is an **ordered, immutable sequence of Unicode characters**.

```python
s = "Hello"
```

Strings support:

* Indexing
* Slicing
* Iteration
* Concatenation
* Various built-in methods

Example:

```python
s[0]
# 'H'

s[1:4]
# 'ell'
```

---

# 12. String Methods

## Searching

### `find()`

Returns the lowest index where the substring is found.

Returns `-1` if the substring is not found.

```python
str.find(substring, start, end)
```

Example:

```python
"hello".find("ll")
# 2
```

---

### `index()`

Similar to `find()`, but raises `ValueError` if the substring is not found.

```python
str.index(substring, start, end)
```

---

### `count()`

Counts the number of occurrences.

```python
str.count(substring)
```

Example:

```python
"banana".count("a")
# 3
```

---

## Alignment

### `ljust()`

```python
str.ljust(width, fillchar)
```

Aligns the string to the left.

### `rjust()`

```python
str.rjust(width, fillchar)
```

Aligns the string to the right.

### `center()`

```python
str.center(width, fillchar)
```

Centers the string.

---

## Zero Padding

### `zfill()`

```python
str.zfill(width)
```

Pads the string with zeros on the left.

```python
"42".zfill(5)
# '00042'
```

---

## Removing Characters

### `strip()`

Removes specified characters from both ends.

```python
str.strip(chars)
```

Without an argument, it removes leading and trailing whitespace.

```python
"  hello  ".strip()
# 'hello'
```

---

## Replacing

### `replace()`

```python
str.replace(old, new, count)
```

`count` is optional.

Example:

```python
"banana".replace("a", "o")
# 'bonono'
```

---

## Joining

### `join()`

```python
separator.join(iterable)
```

Example:

```python
"-".join(["A", "B", "C"])
# 'A-B-C'
```

> `join()` joins the elements of an iterable. It does **not** simply add a character between each character unless the string itself is used as the iterable.

---

## Splitting

### `split()`

```python
str.split(separator, maxsplit)
```

Both arguments are optional.

Example:

```python
"a,b,c".split(",")
# ['a', 'b', 'c']
```

---

## Prefix and Suffix

### `startswith()`

```python
str.startswith(prefix, start, end)
```

### `endswith()`

```python
str.endswith(suffix, start, end)
```

---

## Removing Prefix and Suffix

### `removeprefix()`

```python
str.removeprefix(prefix)
```

### `removesuffix()`

```python
str.removesuffix(suffix)
```

---

## Partitioning

### `partition()`

```python
str.partition(separator)
```

Returns a tuple:

```text
(before, separator, after)
```

Example:

```python
"hello-world".partition("-")
# ('hello', '-', 'world')
```

---

# 13. String Case Methods

### `capitalize()`

Capitalizes the first character and converts the remaining characters to lowercase.

```python
"hello WORLD".capitalize()
# 'Hello world'
```

### `upper()`

Converts characters to uppercase.

```python
"hello".upper()
# 'HELLO'
```

### `lower()`

Converts characters to lowercase.

```python
"HELLO".lower()
# 'hello'
```

### `casefold()`

Performs aggressive case conversion, mainly useful for **case-insensitive comparisons**.

```python
"HELLO".casefold()
# 'hello'
```

### `title()`

Capitalizes the first character of each word.

```python
"hello world".title()
# 'Hello World'
```

### `swapcase()`

Converts uppercase characters to lowercase and lowercase characters to uppercase.

```python
"Hello".swapcase()
# 'hELLO'
```

---

# 14. String Checking Methods

### `isalpha()`

Returns `True` if all characters are alphabetic and there is at least one character.

```python
"Hello".isalpha()
# True
```

### `islower()`

Checks whether all cased characters are lowercase.

### `isupper()`

Checks whether all cased characters are uppercase.

---

# 15. ASCII Codes

Common ASCII ranges:

| Characters | ASCII Range |
| ---------- | ----------: |
| `0 - 9`    |   `48 - 57` |
| `A - Z`    |   `65 - 90` |
| `a - z`    |  `97 - 122` |

Python functions:

```python
ord('A')
# 65

chr(65)
# 'A'
```

---

# 16. List

A **list** is an ordered, mutable collection that can contain heterogeneous elements.

Example:

```python
l1 = [1, "Hello", 3.14, True]
```

### Characteristics

* Ordered
* Mutable
* Index-based
* Supports slicing
* Can contain duplicate elements
* Can contain heterogeneous data types

---

## List Slicing

Syntax:

```python
list[start:stop:step]
```

Example:

```python
l = [1, 2, 3, 4, 5]

l[1:4]
# [2, 3, 4]
```

### Reverse a List

```python
l[::-1]
```

---

## List Methods

### `append()`

Adds one element to the end.

```python
list.append(element)
```

---

### `extend()`

Adds elements from an iterable.

```python
list.extend(iterable)
```

Example:

```python
l = [1, 2]
l.extend([3, 4])

# [1, 2, 3, 4]
```

---

### `index()`

Returns the index of the first occurrence.

```python
list.index(element, start)
```

---

### `remove()`

Removes the first occurrence of an element.

```python
list.remove(element)
```

---

### `pop()`

Removes and returns an element.

```python
list.pop(index)
```

`index` is optional. By default, the last element is removed.

```python
l = [1, 2, 3]

l.pop()
# 3
```

---

### `clear()`

Removes all elements.

```python
list.clear()
```

---

### `reverse()`

Reverses the list in place.

```python
list.reverse()
```

---

### `sort()`

Sorts the list in place.

```python
list.sort(*, key=None, reverse=False)
```

Examples:

```python
numbers.sort()
```

```python
words.sort(key=str.lower)
```

```python
words.sort(key=len)
```

---

### `count()`

Counts occurrences of an element.

```python
list.count(element)
```

---

# 17. List Comprehension

List comprehension provides a concise way to create lists.

Syntax:

```python
[expression for item in iterable if condition]
```

Example:

```python
l1 = [x**2 for x in range(1, 5) if x % 2 == 0]
```

Result:

```python
[4, 16]
```

---

# 18. Tuple

A **tuple** is an ordered, immutable collection.

Example:

```python
T1 = (1, 2, 3, 4, 5)
```

### Characteristics

* Ordered
* Immutable
* Index-based
* Supports slicing
* Can contain heterogeneous elements
* Can contain duplicate elements

Once a tuple is created, its elements cannot be modified, added, or removed.

---

## Tuple Packing

Packing means grouping multiple values into a tuple.

```python
T1 = 1, 2, 3, 4, 5
```

Equivalent to:

```python
T1 = (1, 2, 3, 4, 5)
```

---

## Tuple Unpacking

Unpacking means assigning tuple elements to multiple variables.

```python
a, b, c = (1, 2, 3)
```

### Extended Unpacking

```python
a, b, *c = (1, 2, 3, 4, 5)
```

Result:

```python
a = 1
b = 2
c = [3, 4, 5]
```

---

# 19. Set

A **set** is a mutable collection of unique elements.

Example:

```python
s = {1, 2, 3}
```

### Characteristics

* No indexing
* No slicing
* Does not allow duplicate elements
* Mutable
* Supports set operations such as union, intersection, and difference

Example:

```python
a = {1, 2, 3}
b = {3, 4, 5}

a | b   # Union
a & b   # Intersection
a - b   # Difference
```

> A set itself is mutable, but its elements must be hashable.

---

# 20. Dictionary

A **dictionary** stores data as **key-value pairs**.

Example:

```python
student = {
    "name": "John",
    "age": 20
}
```

### Characteristics

* Mutable
* Preserves insertion order
* Accessed using keys
* Keys must be hashable
* Values can be of any type
* Keys must be unique

Accessing a value:

```python
student["name"]
# 'John'
```

---

# 21. Types of Errors

There are three broad categories of errors commonly discussed in programming.

## 21.1 Syntax Error

Occurs when the code violates Python's syntax rules.

Example:

```python
if True
    print("Hello")
```

Python cannot parse the program correctly.

---

## 21.2 Logical Error

The program executes successfully but produces an incorrect result because the logic is wrong.

Example:

```python
a = 10
b = 20

result = a - b
```

If the intended operation was addition, the program is logically incorrect even though there is no syntax error.

---

## 21.3 Runtime Error

Occurs while the program is executing.

Examples:

```python
TypeError
KeyError
ValueError
ZeroDivisionError
IndexError
```

Example:

```python
10 / 0
```

Raises:

```text
ZeroDivisionError
```

---

# 22. Error Handling

## Why Do We Need Error Handling?

A robust program should handle expected errors gracefully instead of crashing unexpectedly.

Error handling can:

* Prevent unexpected program termination
* Provide meaningful error messages
* Guide users to enter valid input
* Allow cleanup of resources
* Improve application reliability

---

# 23. Exception Handling

Basic structure:

```python
try:
    # Code that may raise an exception
    result = perform_operation()

except Exception as e:
    # Handle the exception
    print(e)

else:
    # Executes when no exception occurs
    return result

finally:
    # Cleanup code
    close_resource()
```

### `try`

Contains code that may raise an exception.

### `except`

Handles an exception.

### `else`

Runs only when no exception occurs in the `try` block.

### `finally`

Runs regardless of whether an exception occurred.

---

# 24. Raising Exceptions

Use `raise` to explicitly raise an exception.

```python
raise ValueError("Invalid value")
```

Example:

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
```

> Inside an `except` block, `raise` by itself re-raises the currently handled exception. `raise e` also raises that exception, but a bare `raise` is generally preferred when you want to preserve the original traceback context.

---

# 25. User-Defined Exceptions

User-defined exceptions should generally inherit from `Exception`.

Example:

```python
class InvalidAgeError(Exception):
    pass
```

Usage:

```python
def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative")
```

---

# 26. OOP — Object-Oriented Programming

**OOP (Object-Oriented Programming)** is a programming paradigm based on objects and classes.

---

## Class

A **class** is a blueprint for creating objects.

Example:

> A house blueprint describes the structure and layout of a house. Similarly, a class defines the structure and behavior of its objects.

```python
class Car:
    pass
```

---

## Object

An **object** is an instance of a class.

```python
car1 = Car()
```

Here:

* `Car` → Class
* `car1` → Object / Instance

---

## Everything in Python is an Object

Python treats values such as:

```python
10
"Hello"
[1, 2, 3]
```

as objects.

They have:

* A type
* An identity
* A value

---

# 27. Members of a Class

A class commonly contains:

### 1. Data Members / Properties

Represent data associated with an object or class.

Examples:

```python
self.length
self.breadth
```

### 2. Member Functions / Methods

Represent behavior associated with the class.

Example:

```python
def area(self):
    return self.length * self.breadth
```

---

# 28. Encapsulation

**Encapsulation** means bundling data and the methods that operate on that data together within a class.

Example: TV

A TV contains many internal components such as:

- Circuit boards
- Wires
- Processor

All these components and their related functionality are enclosed within the TV's body.

Similarly, in OOP, data and the methods that operate on that data are bundled together inside a class.

Encapsulation = Binding data + functionality together

---

# 29. Abstraction

**Abstraction** means exposing essential functionality while hiding unnecessary implementation details.

Example: TV

When using a TV, we can perform operations such as:

- Increase/decrease volume
- Change channels

We don't need to know how these operations are implemented internally.

For example, when we press the volume-up button:

User
  ↓
Press Volume +
  ↓
TV processes the request
  ↓
Speaker volume increases

The user only needs to know what operation to perform, not how the TV internally performs it.

Abstraction = Hiding implementation details and exposing essential functionality

---

# 30. Data Hiding

**Data hiding** means restricting or controlling direct access to implementation details or internal data.

Python does not provide strict access modifiers like some languages. Instead, it uses conventions and **name mangling**.

---

# 31. `self`

`self` refers to the **current object instance**.

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

When we write:

```python
s1 = Student("John")
```

Python internally passes the object reference to the instance method.

```python
s1.__init__("John")
```

Conceptually, it is similar to:

```python
Student.__init__(s1, "John")
```

> `self` is **not a Python keyword**. It is the conventional name used for the instance reference.

---

# 32. Types of Variables in Classes

Common categories include:

1. Instance variables
2. Class variables
3. Local variables

---

## Instance Variables

Instance variables belong to a particular object.

They are commonly initialized inside `__init__()` using `self`.

```python
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
```

Each object can have different values:

```python
r1 = Rectangle(4, 6)
r2 = Rectangle(6, 8)
```

Here:

```text
r1.length = 4
r2.length = 6
```

---

## Class Variables

Class variables belong to the class and are shared through the class unless an instance shadows the attribute.

```python
class Rectangle:
    count = 0
```

They can be accessed using the class name:

```python
Rectangle.count
```

They exist as class attributes even before an object is created.

---

# 33. Types of Methods

Common method types are:

1. Instance methods
2. Class methods
3. Static methods

---

## Instance Methods

An instance method operates on an object instance.

The first parameter is conventionally `self`.

```python
class Rectangle:
    def area(self):
        return self.length * self.breadth
```

---

## Class Methods

A class method receives the class as its first argument, conventionally named `cls`.

It is decorated using:

```python
@classmethod
```

Example:

```python
class Rectangle:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count
```

It can be called using:

```python
Rectangle.get_count()
```

---

## Static Methods

A static method does not receive `self` or `cls` automatically.

It is decorated using:

```python
@staticmethod
```

Example:

```python
class Rectangle:

    @staticmethod
    def calculate_perimeter(length, breadth):
        return 2 * (length + breadth)
```

It can be called using:

```python
Rectangle.calculate_perimeter(5, 8)
```

A static method can access class attributes through the class name if needed, but it does not automatically receive an instance or class reference.

---

# 34. Complete Class Example

```python
class Rectangle:

    # Class variable
    count = 0

    def __init__(self, length, breadth):
        # Instance variables
        self.length = length
        self.breadth = breadth

        Rectangle.count += 1

    # Instance method
    def area(self):
        return self.length * self.breadth

    # Class method
    @classmethod
    def get_count(cls):
        return cls.count

    # Static method
    @staticmethod
    def calculate_perimeter(length, breadth):
        return 2 * (length + breadth)


r1 = Rectangle(4, 6)
r2 = Rectangle(6, 8)

print(r1.area())
print(Rectangle.get_count())
print(Rectangle.calculate_perimeter(5, 8))
```

---

# 35. Inheritance

**Inheritance** allows a class to acquire and reuse properties and methods from another class.

It promotes **code reusability**.

Example:

```text
             Car
              |
      -----------------
      |               |
   LuxuryCar       SportsCar
```

A `LuxuryCar` can reuse features of `Car` and add additional features.

---

## Example

```python
class Car:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Car started")


class LuxuryCar(Car):

    def __init__(self, brand, sunroof):
        super().__init__(brand)
        self.sunroof = sunroof
```

Here:

* `Car` → Parent / Base / Superclass
* `LuxuryCar` → Child / Derived / Subclass

---

# 36. `super()`

`super()` is commonly used to access methods and constructors of a parent class.

Example:

```python
class Parent:
    def __init__(self):
        print("Parent constructor")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")
```

---

# 37. Data Hiding and Access Specifiers

Python does not have strict access specifiers in the same way as languages such as Java or C++.

Instead, Python uses naming conventions and name mangling.

| Access Level  | Syntax   | Accessibility            | Description                                                                      |
| ------------- | -------- | ------------------------ | -------------------------------------------------------------------------------- |
| **Public**    | `name`   | Anywhere                 | Default. Intended to be accessed from anywhere.                                  |
| **Protected** | `_name`  | Class & subclasses       | Convention indicating that the member is intended for internal/subclass use.     |
| **Private**   | `__name` | Class with name mangling | Python transforms the name using name mangling to make accidental access harder. |

---

## Public

```python
class Student:
    def __init__(self):
        self.name = "John"
```

Can be accessed directly:

```python
s = Student()
print(s.name)
```

---

## Protected

A single underscore indicates a protected-by-convention attribute.

```python
class Student:
    def __init__(self):
        self._name = "John"
```

It can technically still be accessed:

```python
s = Student()
print(s._name)
```

The underscore communicates:

> "This is intended for internal use or subclass use."

---

## Private / Name Mangling

Double underscore triggers name mangling.

```python
class Student:
    def __init__(self):
        self.__name = "John"
```

Direct access:

```python
s = Student()

# AttributeError
print(s.__name)
```

Python internally transforms the name approximately to:

```python
_Student__name
```

Therefore:

```python
print(s._Student__name)
```

can access it.

> This is **not true private access control**. Name mangling primarily prevents accidental name collisions and discourages direct access.

---
