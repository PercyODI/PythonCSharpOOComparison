# Types
- What types does the language support?
- Are both reference and value types supported?
- Can new value types be created?

## Type support
C# supports reference and value types.

Python exclusively supports reference types. When passing objects in Python, they are "Object references passed by value". This means that an object reference copied into a function. They function can modify the object (such as appending a list), but it cannot change the assignment of the object.

## New Value Types
C# makes a clear distinction between value types and reference types. The keyword `class` is used to define a new reference type, where the keyword `struct` is used to define a new value type.


List of Types
-

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## Resources
- https://msdn.microsoft.com/en-us/library/ms173104.aspx
- http://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/
