# Multithreading
>- Threads or Thread-like abilities
>- How is multitasking accomplished?

Both Python and C# provide powerful multithreading abilities. There are two methods that both Python and C# can use for multithreading.

The first method is to start a new thread given a function. Python uses the `thread` module, and has a function called `start_new_thread`, that can take a function and parameters.
```python
import thread

def threadFunc(threadName, delay):
  count = 0
  while count < 12345:
    print "Current Count: " + count
    time.sleep(delay * 1000)
    count += 1

try:
  thread.start_new_thread(threadFunc, ("Thread-1", 3))
  thread.start_new_thread(threadFunc, ("Thread-2", 4))
except:
  print "Error"

while 1:
  pass
```
C# has a similar functionality using the ThreadStart class. This class can be passed a method, and it is converted into a thread that can be started.
```csharp
class threadTesting
{
  public void ThreadFunc(string threadName, int delay)
  {
    int count = 0;
    while(count < 12345)
    {
      Console.WriteLine("Current Count: " + count);
      Thread.Sleep(delay * 1000);
      count++;
    }
  }
  static void Main()
  {
    Thread threadOne = new Thread(() => ThreadFunc("Thread-1", 3));
    threadOne.Start();

    Thread threadTwo = new Thread(() +> ThreadFunc("Thread-2", 4));
    threadTwo.Start();

    while(!threadOne.isAlive || !threadTwo.isAlive);
  }
}
```

## Python
The `Thread` module in Python also contains a class that can be subclassed. When this is used, a run method should exist in the class. When the new thread object is created, a start method is available that will run the run method. Using a whole class allows for self-contained variables in the scope of the object.
```python
import threading

class myThread(threading.Thread):
  def __init__(self, threadName, delay):
    threading.Thread.__init__(self)
    self.threadName = threadName
    self.delay = delay
    self.count = 1

  def run(self):
    print "Current Count: " + self.count
    time.sleep(delay * 1000)
    count += 1

threadOne = myThread("Thread-1", 3)
threadTwo = myThread("Thread-2", 4)

threadOne.start()
threadTwo.start()
```

## C#
C# does not allow subclassing of the Thread class, and instead requires either a method or a lambda passed as a parameter of a new Thread object.

C# does have `async` and `await` operators that allow for very easy asynchronous calls.

Any method that could take a while, such as an API call, can be declared async.
```csharp
public async Task<string> ServerResponse()
{
  //...Code here
  string serverMessage = await CallServer("http://example.com");
  return serverMessage;
}
```
Async methods can either return either a `Task`, a `Task<T>` or `void`. Both `Task` and `void` return types do not return a value. A `void` return type cannot be `awaited`, while a `Task` can. The `Task<T>` type allows for a returned value that is encapsulated in the Task object. A async method has the ability to `await` a method, meaning it will wait until the awaited method finishes.

The is powerful, because it allows programming with specified steps, without complicated closures. The methods all contain the variables and methods that exist in its scope at the time. But the program does not block on the awaiting methods, but instead can continue running, then return to the methods when they have finished.

Two frameworks that utilize this async/await are WebMVC/WebAPI and Xamarin. Both of these frameworks have the async built in, such that the server or phone app do not block on async calls. In the case of Xamarin, you can do non-blocking async calls that can access the user interface in a thread-safe manner!


[:rewind: Back to Table of Contents](../README.md) <!-- BackToC -->

## References
- https://www.tutorialspoint.com/python/python_multithreading.htm
- https://www.tutorialspoint.com/csharp/csharp_multithreading.htm
- http://stackoverflow.com/questions/1923512/threading-does-c-sharp-have-an-equivalent-of-the-java-runnable-interface
- https://msdn.microsoft.com/en-us/library/aa645740(v=vs.71).aspx
- https://msdn.microsoft.com/en-us/library/mt674882.aspx
