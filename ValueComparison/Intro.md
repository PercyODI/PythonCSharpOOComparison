# Comparisons of references and values
>- How are values compared? (i.e. comparing two strings)

## Python
Python provides a way to specify whether to compare by reference or by value. Unlike many languages, these are not additions to the equal operator (such as `===`), but instead are two syntactically and visually different operators.

The first is value comparison. Python uses the common C-like comparison with `==`. This will test if two variables are equal. For example, if you want to test if two strings:
```python
str = "Hello World"

str == "Hello World" # Returns True
```

The opposite of `==` is `!=`. This also complies with the C way of comparison.

The second is reference comparison. Python uses an english-like syntax for reference (or object) comparison with `is`. For example, if you want to test if two objects are the same:
```python
intOne = 12345
intTwo = 9876

intOne is intTwo # Returns False
```

The opposite of `is` is `is not`. So from the previous example, you could compare
```python
intOne is not intTwo # Returns True
```

Because of how Python caches, or interns some values, `is` can give unpredictable results. For example, strings might (but not always) be stored in the same memory location. This helps to speed up string comparisons and saves on memory. But two different strings can point to the same location, meaning they have the same reference, and `is` will return True even though they are different objects.

Another gotcha are small integers. Python caches "small" integers in the same memory location, meaning that `is` would return True even on different objects. The definition of a small integer is dependent on the implementation of Python. One CPython implementation range found is -5 to 256, but you cannot rely on that range.

## C#
In C#, there are two ways to accomplish equality comparison; `==` and `.Equals()`. The `==` operator can be overloaded by classes. Value types defined in the .NET framework do provide a default implementation of `==`, which actually calls `.Equals()` and uses [reflection](../Reflection/Intro.md) to make the comparison.

If the `==` operator has not been overloaded, then it compares object references. This is accomplished by calling `.Equals()` on the object typed as an `object`. Many of the problems that arise in C# comparison has to do with polymorphism. Only objects in the same hierarchy can be compared by value (if they have `==` overloaded). If the two objects being compared only have `object` as a shared parent, then the default `object.Equals()` method is called. `object.Equals()` compares the reference of the object, so instead of comparing values, the objects themselves are compared. Similarly, if two objects that might have a common parent are typed as `object`, then even though there is a overloaded `==` operator, the matching response is the default `object.Equals()`. 

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- https://codeyarns.com/2012/05/01/integer-caching-in-python/
- http://stackoverflow.com/questions/1504717/why-does-comparing-strings-in-python-using-either-or-is-sometimes-produce
- https://blogs.msdn.microsoft.com/csharpfaq/2004/03/29/when-should-i-use-and-when-should-i-use-equals/
