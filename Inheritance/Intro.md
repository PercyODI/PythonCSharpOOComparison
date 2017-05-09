# Inheritance
Both languages support the idea of inheritance. To create a subclass in Python, simply pass the super class in as a parameter to the class. Calling the super constructor is done by referencing the super type, and calling its `__init__` method.

```python
class Animal(object):
  def __init__(self, numLegs, isVertebrate):
    self.numLegs = numLegs
    self.isVertebrate = isVertebrate

class Cat(Animal):
    def __init__(self):
      Animal.__init__(self, 4, True)
```

In C#, it is just as easy to create a subclass. To create a subclass, simply pass the super class in after the colon of the class name. Referencing the super constructor is done using base. This is done to ensure that the super type of this instance is constructed before continuing with the child class.

```csharp
public class Animal
{
  public int NumLegs;
  public bool IsVertebrate;

  public Animal(int numLegs, bool isVertebrate)
  {
    this.NumLegs = numLegs;
    this.IsVertebrate = isVertebrate;
  }
}

public class Cat : Animal
{
  public Cat() : base(4, true)
  {
  }
}
```

## Multiple Inheritance
Python supports the idea of multiple inheritance, where C# does not. In Python, simply listing any other classes you want as a parameter to the class lets you subclass them. The subclass will have the methods and attributes of all of its parent classes.

In multiple inheritance languages, having multiple parents that have the same methods or attributes can cause ambiguity and cannot run. Python solves this problem by allowing the programmer to specify which super class they want to use. Python also has a `super()` method to call a class' parent, based on the order they appear in the definition.

```python
class Cat(Animal, Vertebrate):
  def __init__(self):
    Animal.__init__(self, 4, True)
    Vertebrate.__init__(self, "Mammal")
```

C# does not support multiple inheritance. Instead, a type can implement any number of [Interfaces](../Interfaces/Intro.md). There is also the ability to extend a method. By using extension, a method can be added to an existing type (including primitive types). This is helpful by not polluting the type namespaces, and we don't have to redesign class architecture for special cases.

```csharp
namespace AnimalExtensions
{
  public static class Extension
  {
    public static int GetNumLegs(this Animal a)
    {
      return a.NumLegs;
    }
  }
}
```

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- http://www.python-course.eu/python3_inheritance.php
- https://www.codeproject.com/Tips/709310/Extension-Method-In-Csharp
