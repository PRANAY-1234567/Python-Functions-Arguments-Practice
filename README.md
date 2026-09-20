# Python Functions & Arguments Practice

This repository contains Python practice programs focused mainly on **functions, arguments, variable scope, return statements, loops, and basic data processing**.

The code is written as a learning/practice file with multiple examples demonstrating how Python functions work in different situations.

## Topics Covered

### 1. Positional Arguments

Understanding how values are passed to function parameters based on their position.

```python
def demo(a, b, c):
    print(a, b, c)

demo(10, 20, 30)
```

### 2. Variable Positional Arguments – `*args`

`*args` allows a function to accept any number of positional arguments.

```python
def demo(*args):
    print(args)

demo(1, 2, 3, 4)
```

The arguments are collected into a **tuple**.

The code also demonstrates the difference between:

```python
print(args)
```

and

```python
print(*args)
```

* `print(args)` → displays the arguments in packed/tuple form.
* `print(*args)` → displays the arguments in unpacked form.

---

### 3. Keyword Arguments

Arguments can be passed using parameter names.

```python
def spam(a, b, c):
    print(a, b, c)

spam(a=10, b=20, c=30)
```

The examples also demonstrate restrictions when mixing positional and keyword arguments.

---

### 4. Variable Keyword Arguments – `**kwargs`

`**kwargs` allows a function to accept any number of keyword arguments.

```python
def check(**kwargs):
    print(kwargs)

check(x=900, y="abc", z=[1, 2, 3])
```

The arguments are collected into a **dictionary**.

The code also demonstrates the difference between:

```python
print(kwargs)
```

and:

```python
print(*kwargs)
```

---

### 5. Combining `*args` and `**kwargs`

The practice code demonstrates how a function can accept both variable positional and keyword arguments.

```python
def Both_data(*args, **kwargs):
    print(args, kwargs)

Both_data(1, 2, 3, a=90, b=[1, 2, 3])
```

---

### 6. Positional-Only Arguments `/`

Python allows parameters to be defined as positional-only using `/`.

```python
def show(a, b, /, c):
    print(a, b, c)
```

Here, `a` and `b` must be passed positionally.

```python
show(1, 2, c=3)
```

---

### 7. Keyword-Only Arguments `*`

Parameters after `*` must be passed using keyword arguments.

```python
def demo(a, b, *, c, d):
    print(a, b, c, d)

demo(100, 200, c=900, d=1000)
```

---

### 8. Combining Positional-Only and Keyword-Only Arguments

The code demonstrates the combination of `/` and `*`.

```python
def Think(a, b, /, c, *, d, e):
    print(a, b, c, d, e)
```

* `a`, `b` → positional-only
* `c` → positional or keyword
* `d`, `e` → keyword-only

---

## Return Statements

The code demonstrates how functions can return values.

### Returning One Value

```python
def check():
    x = 9000
    return x

print(check())
```

### Returning Multiple Values

```python
def Operations(x, y):
    return x + y, x - y, x * y, x / y

result = Operations(10, 5)
print(result)
```

Multiple returned values are packed into a **tuple**.

The code also demonstrates an important rule:

> Once a `return` statement executes, the function exits.

Therefore, multiple sequential `return` statements do not all execute.

---

## Variable Scope

The practice examples cover:

* Local variables
* Global variables
* Modifying global variables
* Nested functions
* `global` keyword
* `nonlocal` keyword

### Local Variable

```python
def HII():
    y = 10
    print(y)

HII()
```

`y` exists only inside the function.

### Global Variable

```python
a = 100

def Last_Part():
    print(a)

Last_Part()
```

A function can access a global variable.

### Modifying a Global Variable

The `global` keyword allows a function to modify a global variable.

```python
a = 100

def Last_Part():
    global a
    a = a + 900
    print(a)

Last_Part()
```

---

## Nested Functions

The code also demonstrates functions defined inside other functions.

```python
x = 10

def outer():
    y = 20

    def inner():
        z = 30
        print(x)
        print(y)
        print(z)

    inner()

outer()
```

This example demonstrates how inner functions can access variables from their outer scope.

---

## `nonlocal` Keyword

`nonlocal` is used when an inner function needs to modify a variable belonging to its enclosing function.

```python
def outer():
    y = 20

    def inner():
        nonlocal y
        y = y + 80
        print(y)

    inner()

outer()
```

---

## Loops and Data Processing

The file also contains small programming exercises using:

* `for` loops
* `range()`
* `if` conditions
* Lists
* Dictionaries
* `append()`
* `enumerate()`
* `len()`
* String slicing
* `isinstance()`
* `ord()`

### Example: Odd Numbers

Prints odd numbers from 0 to 30 and stores them in a list.

```python
def Number():
    k = []

    for i in range(0, 31):
        if i % 2 == 1:
            k.append(i)

    return k

print(Number())
```

### Example: Character ASCII/Unicode Values

The `ord()` function is used to get the Unicode value of each character.

```python
def Data(y):
    e = {}

    for i in y:
        e[i] = ord(i)

    return e

print(Data("Good luck"))
```

### Example: `enumerate()`

The code demonstrates how to get both the index and value while iterating through a list.

```python
languages = ["Python", "Java", "SQL", "POWERBI", "EXCEL"]

for index, value in enumerate(languages):
    print(index, value)
```

---

## Type Checking with `isinstance()`

The code demonstrates how to check whether values belong to specific data types.

```python
if isinstance(i, (int, float, complex, bool)):
    total = total + i
```

This is used to calculate the total of numeric values from a mixed list.

---

## String and Dictionary Operations

The final exercise processes a list of words based on their length.

```python
a = ["walmart", "kickout", "punchout", "lovely", "Thought"]

def Check(a):
    d = {}

    for i in a:
        if len(i) % 2 == 0:
            d[i] = i
        else:
            d[i] = i[::-1]

    print(d)

Check(a)
```

### Logic

* If the word length is **even** → store the original word.
* If the word length is **odd** → store the reversed word.

For example:

```text
"abc" → "cba"
"abcd" → "abcd"
```

---

## Key Python Concepts Practiced

| Concept              | Purpose                                    |
| -------------------- | ------------------------------------------ |
| Positional Arguments | Pass values based on position              |
| Keyword Arguments    | Pass values using parameter names          |
| `*args`              | Accept variable positional arguments       |
| `**kwargs`           | Accept variable keyword arguments          |
| `/`                  | Define positional-only parameters          |
| `*`                  | Define keyword-only parameters             |
| `return`             | Send a value back from a function          |
| Local Variable       | Variable defined inside a function         |
| Global Variable      | Variable defined outside functions         |
| `global`             | Modify a global variable inside a function |
| `nonlocal`           | Modify an enclosing function's variable    |
| Nested Functions     | Define a function inside another function  |
| `enumerate()`        | Get index and value while iterating        |
| `isinstance()`       | Check an object's data type                |
| `ord()`              | Get Unicode value of a character           |
| `len()`              | Get length of a sequence                   |
| String Slicing       | Manipulate strings such as reversing       |
| Dictionary           | Store key-value pairs                      |
| List                 | Store multiple values                      |

## Purpose

This file was created as **Python fundamentals practice**, especially for understanding how functions handle different types of arguments and how variable scope works.

It is useful for strengthening Python fundamentals for:

* Data Analyst roles
* QA/Testing roles
* Python interviews
* Automation testing
* General Python programming

## Author

**Pranay Vishwanath Jadhao**

* LinkedIn: [linkedin.com/in/pranayjadhao](https://www.linkedin.com/in/pranayjadhao)
* GitHub: [github.com/PRANAY-1234567](https://github.com/PRANAY-1234567)
