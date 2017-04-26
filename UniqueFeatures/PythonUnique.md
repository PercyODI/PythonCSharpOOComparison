# Python Unique Features

## Dynamic Typing
In contrast to C#, Python uses a dynamically typed system. In this system, variables are bound to objects at run-time, and can be rebound to different objects of different types during the execution of the program.

This makes Python feel very flexible. variables can morph and reference many different types of objects, are you aren't bound by the type from the beginning.

## Strongly Typed
Python is also strongly typed. This requires programmers to be very aware of what types their variables can take. The interpreter will forbid undefined (or not well defined) operations instead of trying to make sense of them. Examples include trying to add a number to a string, or attempting to print something that is not a string.

### Example
```python
name = "Pearse Hutson"
print(name) # "Pearse Hutson"
name = 1.2
print(name) # Error, name isn't a string
```

## Whitespace Code Blocks
Python is known for its whitespace code blocks. Many other languages, such as C#, use curly braces for their code blocks.

```csharp
function doAThing()
{
    // Code block defined by curly braces

    if(1 < 2)
    {
      // Here is another code block inside the other code block
      Console.WriteLine("1 is less than 2");
    }
    else
    {
      Console.WriteLine("1 is not less than 2")
    }
}
```

Instead of using curly braces, Python enforces tabs (defined by a set of spaces). Blocks are all of the same tab level, and blocks end by going back a tab level

```python
def doAThing():
  # Code block defined by white space
  if 1 < 2:
    # Here is another code block inside the other code block
    print("1 is less than 2")
  else:
    print("1 is not less than 2")
```

This leads to what Python enthusiasts believe is much cleaner and more readable code. It is considerably less verbose, but in complex code can be confusing to determine what block you are in. Code also must conform to a white space tab length in order for the interpreter to understand what is and isn't in a block.

Much of what Python enthusiasts see as important in coding can be seen in "The Zen of Python". This Enhancement Proposal reads like a poem, and starts with the following lines:
> Beautiful is better than ugly.
>
> Explicit is better than implicit.
>
> Simple is better than complex.
>
> Complex is better than complicated.
>
> Flat is better than nested.
>
> Sparse is better than dense.
>
> Readability counts.

## Interactive Interpreter (REPL)
Python provides a command line interactive interpreter. This allows programmers to run quick prototypes or small experiments. This is possible because Python is an interpreted language, and doesn't have to be compiled to run.

## First Class Collections
Three common collections are considered to be a first-class variable types; lists, dictionaries, and sets. Creating and using these types are much easier in Python, and as built in types they are more efficient than collections in C#.

```python
# List in Python
aList = [1, 2, 3]

# Dictionary in Python
aDictionary = {"key": "value", "Another key": "Another value"}

# Set in Python
aSet = {1, 2, 3}
```

```csharp
// List in C#
ArrayList<int> aList = new ArrayList<int> {1, 2, 3}

// Dictionary in C#
Dictionary<string, string> aDictionary = new Dictionary<string, string>() {
  {"key", "value"},
  {"Another Key", "Another Value"}
}

// Set in C#
HashSet<int> aSet = new HashSet<int>(){1, 2, 3}
```

## First Class Functions

## Explicit "Magic"
Magic methods are methods that are not invoked directly, but instead are realized behind the scenes. Python handles necessary calls to methods "automagically". In Python, these methods are explicitly marked so that there is less confusion about what is and isn't magical. These methods are surrounded by double underscores, as can be seen in the example below.

```python
class aClass:
  # __init__ is a magic method
  def __init__(self, value):
    self.value = value

  # __del__ is another magic method
  def __del__(self):
    print("An aClass was destroyed")
```

[:arrow_backward: Back to Intro](./Intro.md) <!-- BackOne -->

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- https://pythonconquerstheuniverse.wordpress.com/2009/10/03/static-vs-dynamic-typing-of-programming-languages/
- http://www.python-course.eu/python3_blocks.php
- https://www.python.org/dev/peps/pep-0020/
