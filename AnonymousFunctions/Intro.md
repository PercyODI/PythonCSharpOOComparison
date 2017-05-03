# Anonymous Functions
>- Lambda Expressions
>- Closures
>- Functions as Types

Both Python and C# provides methods of creating and using anonymous functions. They both work by using lambda expressions.

## Python
Python lambda's are not true lambdas, but work in the same way. Unlike C#, Python lambdas can only evaluate a single expression. While this can be a limiting factor, it is a powerful way to run functions such as `filter`, `map`, and `reduce` on lists.

```python
nums = [1, 1, 2, 3, 5, 8, 13]

print(list(map(lambda x: x * 2, nums)))
# Returns [2, 2, 4, 6, 10, 16, 26]
```

## C#
C# has much more powerful anonymous function abilities than Python.

First, C# has the delegate type. The delegate type allows programmers to assign a method to a variable. Extending the delegate type is the lambda expression. A lambda expression can be set as the method to a delegate, but can be used in many other places!

C# allows for asynchronous methods. A lambda can be used as the code block to be run asynchronously.

```csharp
button1.Click += async (sender, e) =>
{
  await CallApi();
  Navigation.Push(new ApiPage());
}
```

As you can see, C# lambdas are an entire code block, and are not limited to one expression like they are in Python. In addition to asynchronous methods, lambdas are often used in LINQ statements, allowing for much more powerful collection queries.

```csharp
var result = db.Products.First((product) => product.Name = "Peppermint");
```

C# lambda expressions do allow for closures, in that any non-function variables can be referenced if they are in scope of the function. Garbage collection is prevented on those objects because the lambda still contains references to them.

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- http://www.secnetix.de/olli/Python/lambda_functions.hawk
- https://msdn.microsoft.com/en-us/library/bb397687.aspx
- https://msdn.microsoft.com/en-us/library/ms173172.aspx
