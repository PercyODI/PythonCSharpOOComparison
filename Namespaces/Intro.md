# Namespaces
Namespaces provide a context for identifiers or symbols. We usually think of the names of variables, fields, or methods as the identifiers that need to be in a namespace. Within a namespace, a name can only have one meaning. Because of this, we can think of namespaces as a mapping of names to objects (or any other identifier).

Namespaces also provide a sense of scope in some languages. Local names exist only in their contained scope, and do not clutter their parent namespaces or the global namespace.

## Python
Namespaces are implemented as Python dictionaries.

Examples of namespaces in Python:
- Global
- Local Names
- Built-in Names
  - Built-in Functions like `abs()` and `cmp()`
  - Built-in Exception names

A name's namespace in Python is identical to its scope. For example, a name declared in a function is scoped to that function, and that function is the name's namespace. When trying to determine a name, Python will start with the innermost scope, and work backwards through any enclosing scopes until it hits the global scope.

Modules are important when discussing Python namespaces. A module is a file containing Python code. When a module is imported, it is given its own namespace to create names, and the module is added to the global list of namespaces.

## C#
C# uses explicit namespaces to organize code. The keyword `namespace` is reserved to declare a namespace. Multiple files and parts of code can be added to a namespace, and namespaces can be nested in other namespaces. Any code not in a namespace is placed in the global namespace.

Namespaces can be brought into scope using the `using` keyword.

## Comparison
Both languages use namespaces. However, Python tends to have  implicit namespaces based on Modules or Classes, where C# has named namespaces that can be arbitrarily added to.

Both languages have the ability to alias any namespace. Python uses `import module as anotherName` to create an alias, where C# uses `using AnotherName = NameSpace;`. Alias' is important when modules or classes could have the same name, but we need to access both.

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- http://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html
- https://docs.python.org/3/tutorial/classes.html
