# Python Unique Features

## Dynamic Typing
In contrast to C#, Python uses a dynamically typed system. In this system, variables are bound to objects at run-time, and can be rebound to different objects of different types during the execution of the program.

This makes Python feel very flexible. variables can morph and reference many different types of objects, are you aren't bound by the type from the beginning.

This requires programmers to be very aware of what types their variables can take. Care must be taken to check parameters for their type to avoid None errors or type errors.

### Example
```python
name = "Pearse Hutson"
print(name) # "Pearse Hutson"
name = 1.2
print(name) # Error, Name isn't a string
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

[:arrow_backward: Back to Intro](./Intro.md) <!-- BackOne -->

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- https://pythonconquerstheuniverse.wordpress.com/2009/10/03/static-vs-dynamic-typing-of-programming-languages/
- http://www.python-course.eu/python3_blocks.php
