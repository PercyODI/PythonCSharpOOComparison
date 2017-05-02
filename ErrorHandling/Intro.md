# Errors and Exception Handling

Python and C# are very similar when it comes to error handling.  They both implement a try-catch exception handling system. Both systems allow a finally block to run whether the try succeeds or fails. They also can check for multiple exception types and perform different actions for each exception.

```python
def CallApi():
  try:
    AjaxCallApi()
    print("API has been called")
  except ApiError as apiEr:
    print("API could not be called")
  finally:
    CloseApiCall()
```

```csharp
public void CallApi()
{
  try
  {
    AjaxCallApi();
    Console.WriteLine("API has been called");
  }
  catch (ApiException apiEx)
  {
    Console.WriteLine("API could not be called");
  }
  finally
  {
    CloseApiCall();
  }
}
```

It is worth noting that when errors occur in Python, the line number is displayed along with a description of the error. Contrast this with C#, where exceptions throw long stack traces that can be hard to debug and do not point out exactly where the error occured.

[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- http://blog.chphilli.net/2010/08/python-vs-c-exceptions.html
