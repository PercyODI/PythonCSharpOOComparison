# C# Unique Features

## Assemblies

## Cross-language Compatibility
The .NET framework includes what is called the Common Language Runtime, or CLR. The CLR is able to convert Common Intermediate Language into machine instructions using a process called Just-In-Time compilation. This ability is powerful because there are many languages that are compiled into Common Intermediate Language code, including C#, VB.NET, C and C++.

This shared runtime allows a programmer in the Windows environment to be familiar with aspects such as memory management, type safety, exception handling, garbage collections, security, and thread management.

## Improved Properties
C# classes can take advantage of Properties, which automatically have default Getters and Setters. These Getters and Setters are easily customizable with the use of a backing variable.

This also leads to the term "Property Bag", where a class is merely a data model with a set of properties attached to it. These are very clean, understandable to other programmers, and easy to expand when needed.
```csharp
class PropertyBag
{
  public int intValue { get; set; }
  public string intString { get; set; }

  private double _backingVar;
  public double BackingVar
  {
    get
    {
      return _backingVar;
    }

    set
    {
      _backingVar = value;
    }
  }
}
```

## First-Class Listeners
Events are built in types in C#. This provides a standard way to provide state changes and notification for objects with automatic listener support (addListener and removeListener). Other languages provide event support through another library or custom solutions.

## Extension Methods
C# provides a way of extending existing types by adding instance methods to a type without modifying the original type, without creating subtypes, or without creating type containers. These extension methods are applied whenever the namespace that the extension exists in is in scope.

The extension system feels a little clunky, but provides an ability that earlier languages did not have.

```csharp
namespace ExtensionMethods
{
  public static class MyExtensions
  {
    public static int WordCount(this String str)
    {
      return str.Split(new char[] { ' ', '.', '?' },
        StringSplitOptions.RemoveEmptyEntries).Length;
    }
  }
}
```

```csharp
using ExtensionMethods;

public class SomeClass
{
  public void Main()
  {
    string s = "This is an Extension Test";
    int i = s.WordCount(); // Returns 5
  }
}
```

## Partial Classes
In addition to extension methods, C# provides the ability to write partial classes. Partial classes allow programmers to split the definition over several files. When the application is compiled, the class is the combination of all of the partial definitions.

```csharp
public partial class PartClass
{
  public int SomeProp { get; set; }

  public void DoSomething()
  {
    return;
  }
}

public partial class PartClass
{
  public void DoSomethingElse()
  {
    return;
  }
}

// PartClass has both DoSomething and DoSomethingElse methods.
```

[:arrow_backward: Back to Intro](./Intro.md) <!-- BackOne -->

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- https://msdn.microsoft.com/en-us//library/bb383977.aspx
- https://msdn.microsoft.com/en-us/library/wa80x488.aspx
