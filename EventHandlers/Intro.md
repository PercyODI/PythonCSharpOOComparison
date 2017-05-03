# Event Handlers
>- Implementation of listeners and event handlers

## Python
Python does not have built in listeners and event handlers. However, events can added to Python using first-class functions. Classes can be built to accept functions, and call a function when an event is thrown.

Many Python libraries have event handler systems, but they are not standardized, and each implement their own system. As we are not including any libraries beyond the standard libraries, they will not be included in this comparison.

## C#
C# provides a powerful event handling system. Events in C# are based on delegates, which are C# solution to first-class functions. A delegate defines parameter types and return type of a method, without defining the method itself. The method can be defined in other methods, or can be assigned anonymously. This gives us the type safety we expect in C#, while still giving us the ability to pass around functions (which was lacking in Java).

C# also provides an `event`. An `event` allows handlers of type defined by a delegate to be fired when certain conditions are met. This allows methods to be added to an event dynamically. This system is built into the .NET framework, and provides a standard way of handling events in C#.

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- http://openbookproject.net/thinkcs/python/english3e/events.html
- http://www.valuedlessons.com/2008/04/events-in-python.html
- https://msdn.microsoft.com/en-us/library/aa645739(v=vs.71).aspx
- https://www.intertech.com/Blog/c-sharp-tutorial-understanding-c-events/
