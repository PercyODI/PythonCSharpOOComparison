# Singleton
>- How is a singleton implemented?
>- Can it be made thread-safe?
>- Can the singleton instance be lazily instantiated?

## Python
Python has several ways to building a singleton.

The first way uses a check in `__init__` to only allow instantiation once. A class method is provided to get the instance, or create it if it hasn't been instantiated yet.
```python
class MySingleton(object):
     INSTANCE = None

     def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")
        # do your init stuff

     @classmethod
     def get_instance(cls):
        if cls.INSTANCE is None:
             cls.INSTANCE = MySingleton()
        return cls.INSTANCE
```
*(Taken from http://amir.rachum.com/blog/2012/04/26/implementing-the-singleton-pattern-in-python/)*

This singleton is lazily instantiated, but is not thread-safe.

A second method, which is considered to be a much better implementation to the others, is use of a metaclass.

```python
class SingletonType(type):
    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
            return cls.__instance

class MySingleton(object):
    __metaclass__ = SingletonType
```
*(Taken from http://amir.rachum.com/blog/2012/04/26/implementing-the-singleton-pattern-in-python/)*

This method provides a way to turn any class into a singleton.  The singleton is created lazily, but is also not thread-safe. Use of the threading library gives us a lock mechanism that could be used to transform the metaclass singleton into a thread-safe version. Such a singleton would like this:

```python
import threading

class SingletonType(type):
    __singleton_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        try:
            return cls.__instance
        except AttributeError:
            with cls.__singleton_lock:
              cls.__instance = super(SingletonType, cls).__call__(*args, **kwargs)
              return cls.__instance

class MySingleton(object):
    __metaclass__ = SingletonType
```

## C#
C# allows for constructors to be private, which helps in the singleton creation process by preventing other classes from instantiating it. While there are several ways to create singletons in C#, by far the easiest is to use the `System.Lazy<T>` type provided in the .NET framework. By default, any `System.Lazy` attribute is lazily instantiated and is thread-safe. All it requires is a delegate method to execute, which can be given anonymously.

```csharp
public class Singleton
{
    private static readonly Lazy<Singleton> lazy =
        new Lazy<Singleton>(() => new Singleton());

    public static Singleton Instance { get { return lazy.Value; } }

    private Singleton()
    {
    }
}
```
*(Taken from http://csharpindepth.com/Articles/General/Singleton.aspx)*

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
- http://lucumr.pocoo.org/2009/7/24/singletons-and-their-problems-in-python/
- http://amir.rachum.com/blog/2012/04/26/implementing-the-singleton-pattern-in-python/
- https://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/
- http://csharpindepth.com/Articles/General/Singleton.aspx
- https://msdn.microsoft.com/en-us/library/dd997286(v=vs.110).aspx
