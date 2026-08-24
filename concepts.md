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
| `list`     | Yes        | Yes     | Yes             | `[1, 2, 3]` |
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

