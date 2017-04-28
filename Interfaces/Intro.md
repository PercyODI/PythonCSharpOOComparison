# Interfaces
>- Interfaces / Protocols
>- What does the language support?
>- What abilities does it have?
>- How is it used?

## Python Interfaces
Python does not support the idea of interfaces. The use of Duck typing means that the Pythonic way of handling a method on an object is to just try to call the method. If the method exists, it will run; otherwise it will raise an exception.

Another important consideration is Python's acceptance of multiple inheritance. Because of this, a class can have multiple parent classes; in languages like C# without multiple inheritance, inheritance can be used to give a class multiple parents.

In response to a request from Python users to have some sort of interface system, Python includes a module called ABC. ABC stands for Abstract Base Classes, and they provide a way to create an abstract class in Python that cannot be instantiated.

A methods of an ABC can either `pass` to a subclass, or can have methods that can be overwritten or extending by calling `super`. Missing methods on a subclass prevent instantiation, which acts like an interface.

## C# Interfaces
C# supports the idea of interfaces. An interface in C# consists of methods, properties, events, and indexers. None of the methods can have an implementation; implementation must be handled by the subclass. In addition, interfaces methods are assumed to be `public`, and cannot be static.

```csharp
interface IMovable
{
  int Move();
}
```

In C#, a class can implement any number of interfaces, and can be typed as any of the interfaces it implements. This is important, because classes cannot be grouped if they are of different types, and if classes all contain the same method, they must be able to be called by a type that declares that method.

```csharp
public class Car : IMovable
{
  public int Move()
  {
    return 70;
  }
}
```

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- http://dirtsimple.org/2004/12/python-interfaces-are-not-java.html
- https://nedbatchelder.com/text/pythonic-interfaces.html
- https://pymotw.com/2/abc/
- https://msdn.microsoft.com/en-us/library/ms173156.aspx
