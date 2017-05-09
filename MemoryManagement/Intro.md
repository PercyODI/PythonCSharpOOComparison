# Memory Management
>- How is it handled?
>- How does it work?
>- Garbage collection?
>- Automatic reference counting?

## Python
Python handles memory management internally through the "Python Memory Manager". This manager is a private heap that contains all python objects and data structures.

Because Python is not a standardized language, and many different implementations exists, no guarantees can be made about garbage collections. In CPython, which is considered the main implementation, a combination of Reference Counting and Mark-And-Sweep are used. However, Jython and IronPython use a pure garbage collection system.

## C#
C# itself does not handle memory, but instead the Common Language Runtime handles all memory management. C# uses garbage collection which, like Java, is unpredictable and can occur at any time. Garbage collection runs periodically to remove unreferenced objects, or when certain conditions are met, such as low physical memory or object allocation surpasses a threshold.

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- https://docs.python.org/3/c-api/memory.html
- http://stackoverflow.com/questions/9062209/why-does-python-use-both-reference-counting-and-mark-and-sweep-for-gc
- https://msdn.microsoft.com/en-us/library/ee787088(v=vs.110).aspx
- https://msdn.microsoft.com/en-us/library/ms228629(v=vs.90).aspx
