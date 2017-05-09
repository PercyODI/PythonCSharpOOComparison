# Properties
>- Getters and setters...write your own or built in?
>- Backing variables?
>- Computed properties?

## Getters and setters
The "Pythonic" way of handling properties is to access the directly. Python does not enforce access modifiers, so all properties are publicly accessible at all times. There are conventions to use an underscore prefix to identify something as a private variable, nothing prevents access to the variable. Python enthusiast have even labeled Getters and Setters as *Python Anti-Patterns*.

C# has very simple properties. To create a property, simply follow a field with `{ get; set; }`. You can even specify whether you want only a getter `{ get; }`, or a setter `{ set; }`.

```csharp
class PropertyExample
{
  public int IntProperty { get; set; } // Has a getter and setter
  public string StrProperty { get; } // Has a getter, but no setter
}
```

These properties can be accessed like any normal field.
```csharp
class main{
  var propEx = new PropertyExample();
  propEx.IntProperty = 1;
  Console.WriteLine(propEx.IntProperty); // Prints "1"
}
```

## Computed Properties
Python does support the idea of a property, and provides a property decorator to help control property values and to handle computed values. Despite labeling getters and setters as *Anti-Patterns*, the property decorator provides a getter function and a setter function. Using these functions often requires the use of a backing variable, indicated with an underscore before it's name. Unlike C#, this backing variable cannot be declared private, and is publicly available and modifiable.

```python
class Fahrenheit:
  def __init__(self, temperature = 0):
    self._temperature = temperature

  @property
  def celsius(self):
    return (self._temperature - 32)/1.8

  @celsius.setter
  def celsius(self, value):
    if value < -273:
      raise ValueError("Temperature below -273 C is not possible.")
    self._temperature = (value * 1.8) + 32
```

C# actually resembles Python in a lot of ways when it comes to computed properties. Backing variables are used, and conventionally are marked by an underscore in front of their name. However, backing variables in C# can be declared private, so there is no risk of outside manipulation. All modification has to be done through the getter, setter, or within the class itself. Computed values can be done through the getter or setter, just like in Python.

Note: in the setters of C# properties, `value` is an implicit parameter containing the value from the code.

```csharp
class Fahrenheit
{
  private double _temperature;
  public double Temperature
  {
    get { return _temperature }; set { _temperature = value };
  }

  public double Celsius
  {
    get {
      return (Temperature - 32) / 1.8;
    },

    set {
      if(value < -273)
        throw ValueException("Temperature below -237 C is not possible.");
      Temperature = (value * 1.8) + 32;
    }
  }
  public Fehrenheit(temperature = 0)
  {
    this.Temperature = temperature;
  }
}
```

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- https://docs.quantifiedcode.com/python-anti-patterns/correctness/implementing_java-style_getters_and_setters.html
- https://www.programiz.com/python-programming/property
