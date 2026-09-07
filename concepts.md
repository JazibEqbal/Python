Program: A set of instructions performed on some data.<br>

Statically typed language: The data type of variable is pre-decided/declared. E.g: int x = 10; <br>
Dynamically typed language: The data type of variable is not pre-decided/declared else they are evaluated at runtime E.g: x = 10<br>

In python suppose, a,b,c = 1, 1, 1: python allocates only one memory and all variables points to the same id/address.<br>

Python is case-sensitive.

### Data Types:
| Type       | Ordered    | Mutable | Index-Based     | Example     |
| ---------- |------------| ------- |-----------------| ----------- |
| `int`      | —          | —       | —               | `10`        |
| `float`    | —          | —       | —               | `3.14`      |
| `complex`  | —          | —       | —               | `2+3j`      |
| `bool`     | —          | —       | —               | `True`      |
| `str`      | Yes        | No      | Yes             | `"Hello"`   |
| `_list.py`     | Yes        | Yes     | Yes             | `[1, 2, 3]` |
| `tuple`    | Yes        | No      | Yes             | `(1, 2, 3)` |
| `set`      | No         | Yes     | No              | `{1, 2, 3}` |
| `dict`     | Yes (3.7+) | Yes     | No (using keys) | `{"a": 1}`  |
| `NoneType` | —          | —       | —               | `None`      |

Literals/Constants: Direct value assigned to a variable. e.g. a = 6.

x = 5 + 6, 5 & 6 are operands and + is operator

When we are using compound conditional operators such as `and` or `or`. If the first condition is false for `and` true for `or` then
it won't check another conditions. This is only called as short circuit.

Bitwise &: if both are 1 then 1 else 0. 10 & 13 → 8 → format(8, ''b') → 1000

Bitwise !: if both are 0 then 0 else 1. 10 & 13 → 15 → format(15, ''b') → 1111

Left Shift: Number gets doubled on 1 shift. i.e `a << n == (2 ^ n) * a`<br>
e.g: a = 10; a in binary is = 1010
a << 1 = 10100 = 20
a << 2 = 101000 (40)

Right Shift: Number gets doubled on 1 shift. i.e `a << n == a / (2 ^ n)`<br>
e.g: a = 10; a in binary is = 1010
a << 1 = 10100 = 20
a << 2 = 101000 (40)

Literals are only created once. Any literals declared with the same value will point to the same literal i.e.,`x = 25 y = 25` 
for y new memory won't be allocated, instead it will point to the same memory location 
as x. so statement `x is y` will stand true.

`range(start, stop, step)`:
    start is optional, by default 0
    step is optional, by default 1.

### String Methods:
    str.find(substring, start, end): -1 when substring not found
    str.index(substring, start, end): error when substring not found
    str.count()
    str.ljust(width, fillCharacter)
    str.rjust(width, fillCharacter)
    str.center(width, fillCharacter)
    str.zfill(width): fillCharacter is 0
    str.strip(char): if spaces then it will remove spaces from both side, unless char is specified.
    str.replace(old, new, count): count is optional
    str.join(char): will add each letter with char in between
    str.split(char, maxsplit)
    srr.startswith(prefix, start, end)
    srr.endswith(prefix, start, end)
    str.removeprefix(prefix)
    str.removesuffix(suffix)
    str.partition(seperator)
    str.capitalize(): Only 1st letter as Capital
    str.upper(): all letter as CAPITAL
    str.lower()/str.casefold(): all letter as capital
    str.title(): every first char of word as Capital
    str.swapcase(): converts upper case as lower and vice versa
    str.isalpha(): only alphabets
    str.islower()
    str.isupper()


ASCII Codes:
 - 0 - 9: 48 - 7
 - A - Z: 65 - 90 
 - a - b: 96 - 122

List:
 - Ordered collection of heterogeneous elements, mutable
 - list are heterogeneous (can have element of different data types)
 - list slicing: [start, stop, step], [::-1] (reverse order)
 - list.append(element): adds an element at the end of an list
 - list.extend(iterable): adds any iterable/group at the end of an list
 - list.index(element, index)
 - list.remove(element)
 - list.pop(index): index is optional, by default deletes last element
 - list.clear(): removes all elements from an list
 - list.reverse()
 - list.sort(*, key=None, reverse=False): key = len, key = str.lower
 - list.count(element)
 - list comprehension: l1 = [ x**2 for x in range(1, 5) if x % 2 == 0]

Tuple:
 - Ordered collection of heterogeneous elements, immutable
 - once created, cannot be modified/added
 - tuple packing: T1 = 1, 2, 3, 4, 5 --> (1, 2, 3, 4, 5)
 - tuple unpacking: a, b, *c = T1 --> a = 1, b = 2, c = [3, 4, 5]

Set:
 - Unordered collection of heterogeneous elements, mutable
 - no indexing & slicing

Dictionary:
 - Ordered collection of heterogeneous elements, mutable

### Types of Errors:
 - Syntax Error
 - Logical Error
 - Runtime Error (program executes but throws Traceback call) (TypeError, KeyError, ValueError etc.)

Need of error handling?<br>
Program/application shouldn't crash else it should guide the user to input the value correctly via prompt/labels etc.

```python
def exception_handling():
    try:
        open resource
        use resource
    except Exception as e:
        raise e
    else:
        return result
    finally:
        close resource
```

User defined exceptions must be inherited/derived from Exception class.

## OOPs (Object-Oriented Programming)

 - Class: A blueprint. E.g., A blueprint of a house design/layout.<br>
 - Object: Instances of the class. Based on blueprint. E.g., A house made from of the blueprint of the class.
 - Everything in python are objects.
 - A class is made up of twp things:
    - Data members / properties
    - Member functions / methods
 - Encapsulation: Binding together data members & member functions inside a class.
 - Abstraction: Hiding data and functionality. 
 - E.g., TV
   - Everything, all functionality, circuit is enclosed in a box which is encapsulation.
   - User can perform operations without knowing the working of operation such as volume change, channel change which is nothing but abstraction.
   - What it is doing up with the data internally we don't know, this is data hiding.
 - Self is the reference to the current object. When we create the object, the same object's reference is passed to self and can be checked with id. Self is not a keyword.
 - Types of variables: Instance variables, class variable and static variables.
 - Types of methods: Instance methods, class methods and static methods.
 - Instance variables are created or declared inside __init__(), declared and accessed using self. Instance variables can be created outside of __init()__ but in order to use it, you must call the function before using.
 - Instance methods first parameter must be self
 - Class/Static variables: Information of class. mostly declared before init method. class variables are accessed using class name inside instance methods. Are present even without creation of object and act as a share data/property across all objects.
 - Class methods are accessed using class name and is decorated by @classmethod decorator.
 - Static methods: declared without self with decorator @staticmethod. Purpose is to get some info, without creating object. E.g, know interest without opening bank account. Static methods can't access members of a class because there is no self. 
 - ```python
    class Rectangle:
        count = 0 # class variable
        def __init(self, l, b):
            # instance variables
            self.length = l
            self.breadth = b
    
        # instance method
        def area(self):
            return self.length * self.breadth
   
        @classmethod
        def get_count(cls):
            return cls.count
        
        @staticmethod
        def cal_perimeter(l, b):
            return 2 * (l + b)
    
    r1 = Rectangle(4, 6)
    r2 = Rectangle(6, 8)
    # print(r1.get_count())
    print(Rectangle.get_count())
    print(Rectangle.cal_perimeter(5, 8))
    ```