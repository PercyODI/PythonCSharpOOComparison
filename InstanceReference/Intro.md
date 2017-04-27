# Instance Reference
- Instance reference name in data type (class)

## Python
Python uses `self` to refer to an instance of a class, and uses `clr` to refer to a class member.

Python requires that any methods in a class first take self as a parameter. Every time a method is called, `self` is literally passed in as a object reference just like any other parameter.

It is also important to note that `self` and `clr` are not keywords, and could be replaced by any name. It is only by convention that we exclusively use those two names.

## C#
C# uses `this` to refer to an instance of a class. Class members are designated as `static`.

Unlike Python, `this` is assumed to be present in any method invoked by an instance.

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html
