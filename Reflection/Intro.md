# Reflection
>- What reflection abilities are supported?
>- How is reflection used?

## Python
Python has excellent reflective abilities. Reflection is accomplished in two different ways. The first way is to use reflective functions. These include functions like `type()`, `isinstance()`, `callable()`, `dir()`, and `getattr()`.

The second form of reflection in Python is by using it's duck typing system. Instead of testing for a class or a method, simply call the method. If it doesn't throw an exception then it has that method. Otherwise it doesn't.

## C#
C# also has reflective abilities. Unlike in Python, C# reflection must be explicit (i.e. no duck typing). C# provides a reflection API that can be used to access reflective abilities such as getting types or properties. Commonly, these methods are accessed as static methods on the class, but must be cast to the reflective API types.

It is valuable to note that in C#, reflection is not limited to public members. Private and other access level members can be accessed by setting flags in the reflection API.

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- https://en.wikibooks.org/wiki/Python_Programming/Reflection
- https://www.javatpoint.com/c-sharp-reflection
