# interfaces
An interface is a completely "abstract class", which can only contain abstract methods and properties (with empty bodies).

- Like abstract classes, interfaces cannot be used to create objects (in the example above, it is not possible to create an "IAnimal" object in the Program class)

- An interface cannot contain a constructor (as it cannot be used to create objects)

- To access the interface methods, the interface must be "implemented" (kinda like inherited) by another class. Interface methods do not have a body - the body is provided by the "implement" class

- Note that you do not have to use the override keyword when implementing an interface.

- Interfaces can contain properties and methods, but not fields/variables

- By default, members of an interface are abstract and public.

It is considered good practice to start with the letter "I" at the beginning of an interface, as it makes it easier for yourself and others to remember that it is an interface and not a class.

# Why And When To Use Interfaces?
1) To achieve security - hide certain details and only show the important details of an object (interface).

2) C# does not support "multiple inheritance" (a class can only inherit from one base class). However, it can be achieved with interfaces, because the class can implement multiple interfaces. Note: To implement multiple interfaces, separate them with a comma 

# Multiple Interfaces

C# does not support "multiple inheritance" (a class can only inherit from one base class). 
However, it can be achieved with interfaces, because the class can implement multiple interfaces. 

To implement multiple interfaces, separate them with a comma:

interface IFirstInterface 
{
  void myMethod(); // interface method
}

interface ISecondInterface 
{
  void myOtherMethod(); // interface method
}

// Implement multiple interfaces
class DemoClass : IFirstInterface, ISecondInterface 
{
  public void myMethod() 
  {
    Console.WriteLine("Some text..");
  }
  public void myOtherMethod() 
  {
    Console.WriteLine("Some other text...");
  }
}

class Program 
{
  static void Main(string[] args)
  {
    DemoClass myObj = new DemoClass();
    myObj.myMethod();
    myObj.myOtherMethod();
  }
}