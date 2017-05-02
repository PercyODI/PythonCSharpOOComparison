# Null / None references
>- Which does the language use?
>- Does the language have features for handling null/none references?

## Python
Python uses `None` for no reference. None is special though; it is a singleton object, like `True` and `False`. Because `None` is a singleton, the Pythonic way of checking for `None` is to use the identity reference `is` or `is not`.
```python
variable = None

if variable is not None:
  # This code block will never run
```

## C#
In C#, `null` is a literal that represents no reference. `null` is a default value of any reference variables, but primitive types such as `int` or `DateTime` cannot be null. C# does provide Nullable Types that can convert a primitive type into a container that can be null.

Unlike Python, C# provides several ways of working with null. The first is null propagation. The null propagation operator is `?.`, and it allows programmers to attempt to access objects and fields that might or might not be null.
```csharp
var result = objectOne?.objectTwo?.objectThree
```

If objectOne or objectTwo are null, null propagation prevents the dreaded NullReference Exception, and instead just assigns null to `result`. While this could have been done with if conditions checking for null, this is much more concise, and allows for deeper levels of null checking.

In addition to the null propagation operator, C# also provides the null-coalescing operator. The null-coalescing operator is `??`, and it allows programmers to write conditional statements around null.

Using `??`, the returned value is the left-hand side unless it is null, in which case the returned value is the right-hand side. This is extremely important since primitive types cannot be null. This allows assignment of primitive typed variables with values that could be null.

```csharp
int? x = null;

int variable == x ?? 0;
```

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- https://docs.python.org/3.6/c-api/none.html
- http://python-history.blogspot.com/2013/11/story-of-none-true-false.html
- http://www.i-programmer.info/news/89-net/7016-c-gets-a-new-operator-safe-navigation.html
- https://msdn.microsoft.com/en-us/library/ms173224.aspx
