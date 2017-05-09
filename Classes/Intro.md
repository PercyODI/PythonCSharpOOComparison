# Classes
>- Defining
>- Creating New Instances
>- Constructing / Initializing
>- Destructing / De-Initializing

## Defining
Classes in Python are defined by using the keyword `class`.
```python
class Employee:
  def __init__(self):
    self.company = "ABC Co."

  def getCompany(self):
    return self.company
```

Classes in C# are defined with a access modifier and the `class` keyword.
```csharp
public class Employee
{
  public string company;

  public Employee()
  {
    this.company = "ABC Co.";
  }

  public string getCompany()
  {
    return company;
  }
}
```

## New instance
Both languages make it simple to create a new instance of a class. The only difference is the use of the `new` keyword in C#.
```python
# Python new instance
newEmp = Employee()
```

```csharp
// C# new instance
newEmp = new Employee();
```
## Constructing and Initialization
As you can see from the last two examples, constructors look very different in each language. Python uses the magic method `__init__()`. Any parameters that need to be passed to a Python constructor go in the parameter list of `__init__` after `self`.

Because Python does not allow overloading of methods, only one constructor is allowed. There are a couple work-arounds to this limitation. One solution is to have a list of parameters with default values set.
```python
class Employee:
  def __init__(self, company = "ABC Co.", name = None):
    self.company = company
    self.name = name if name is not None else ""
```

Another option is to use class methods that act as multiple constructors. The class methods return an instance of the class with some parameters abstracted away.
```python
class Employee:
  def __init(self, company, name):
    self.company = company
    self.name = name

  @classmethod
  def abcEmployee(cls, name):
    return cls("ABC Co.", name)

# Example usage
newEmp = Employee.abcEmployee("Name")
```

C# instances are constructed using a constructor. Constructors are public methods with the same name as the class. C# also allows overloading of constructors, so different constructors can be made to fit different situations and have the ability to call each other.
```csharp
public class Employee
{
  public string company;
  public string name;

  public Employee()
  {
    this.company = "ABC Co.";
    this.name = "";
  }

  public Employee(string name)
  {
    this.company = "ABC Co.";
    this.name = name;
  }

  public Employee(string company, string name)
  {
    this.company = company;
    this.name = name;
  }

  public string getCompany()
  {
    return company;
  }
}
```

## Destructing
Both Python and C# allow for code to be run when an object is about to be destroyed. Python uses the magic method `__del__`, where C# uses the use of the tilde and the class name `~Employee()`. In both languages a destructor is invoked automatically, cannot take parameters, and cannot be overloaded.

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->
