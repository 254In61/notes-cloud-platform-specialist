# Overview
A method is a block of code which only runs when it is called.

You can pass data, known as parameters, into a method.

Methods are used to perform certain actions, and they are also known as functions.

Why use methods? To reuse code: define the code once, and use it many times.

# Create a Method
A method is defined with the name of the method, followed by parentheses (). 

C# provides some pre-defined methods, which you already are familiar with, such as Main(), but you can also create your own methods to perform certain actions:

Example :

// create a method inside the Program class:
class Program
{
  static void MyMethod()    ---> MyMethod() is the name of the method
  {
    // code to be executed
  }
}

--> static means that the method belongs to the Program class and not an object of the Program class. 

--> void means that this method does not have a return value. 

=> In C#, it is good practice to start with an uppercase letter when naming methods, as it makes the code easier to read.

# You can have methods outside a class in C#?

No — in C# you cannot have a method at the top level of a file (outside a class/struct/record/module) like you can in Python, Go, or JavaScript.

Every method in C# must belong to a type.

public class Calculator
{
    public int Add(int a, int b)
    {
        return a + b;
    }
}

# Parameters and Arguments

Information can be passed to methods as "parameter". 
Parameters act as variables inside the method.

They are specified after the method name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.

When a parameter is passed to the method, it is called an argument.

# Default Parameter Value

You can also use a default parameter value, by using the equals sign (=).

If we call the method without an argument, it uses the default value ("Norway"):

static void MyMethod(string country = "Norway") 
{
  Console.WriteLine(country);
}

static void Main(string[] args)
{
  MyMethod("Sweden");
  MyMethod("India");
  MyMethod();
  MyMethod("USA");
}

// Sweden
// India
// Norway
// USA

# return values or void
We used the void keyword to indicate that the method should not return a value.

If you want the method to return a value, you can use a primitive data type (such as int or double) instead of void, and use the return keyword inside the method:

# Named Arguments
It is also possible to send arguments with the key: value syntax.

That way, the order of the arguments does not matter:

static void MyMethod(string child1, string child2, string child3) 
{
  Console.WriteLine("The youngest child is: " + child3);
}

static void Main(string[] args)
{
  MyMethod(child3: "John", child1: "Liam", child2: "Liam");
}

// The youngest child is: John

# Method Overload

Instead of defining two methods that should do the same thing, it is better to overload one.

When you use method overloading in C#, the compiler can tell the difference between the methods.

It does this by looking at the method signature, which includes:
- Method name
- Number of parameters
- Parameter types
- Parameter order

Under the hood 🛠️

- Each overloaded method is compiled into separate methods with unique metadata signatures in the IL (Intermediate Language).

- The CLR (runtime) doesn’t get confused, because each version is uniquely identified.

Example : 

public class Calculator
{
    public int Add(int a, int b)        // signature: Add(int, int)
    {
        return a + b;
    }

    public double Add(double a, double b)  // signature: Add(double, double)
    {
        return a + b;
    }

    public int Add(int a, int b, int c) // signature: Add(int, int, int)
    {
        return a + b + c;
    }
}

What happens at compile time?

1. If you call:

Calculator calc = new Calculator();
Console.WriteLine(calc.Add(3, 4));

The compiler sees Add(int, int) and chooses the first method.

2. If you call:

Console.WriteLine(calc.Add(3.2, 4.5));

The compiler sees Add(double, double) and chooses the second method.

3. If you call:

Console.WriteLine(calc.Add(1, 2, 3));

The compiler sees Add(int, int, int) and chooses the third method.
