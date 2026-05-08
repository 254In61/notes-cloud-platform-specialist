# syntax
using System;      ----> we can use classes from the System namespace.

namespace HelloWorld ------> namespace is used to organize your code, and it is a container for classes and other namespaces.
{
  class Program ----> a container for data and methods, which brings functionality to your program. Every line of code that runs in C# must be inside a class.
  {
    static void Main(string[] args) ----> Main method. Any code inside its curly brackets {} will be executed.
    {
      Console.WriteLine("Hello World!");    ----> Console is a class of the System namespace, which has a WriteLine() method that is used to output/print text. 
    }
  }
}

- Every C# statement ends with a semicolon ;.
- If you omit the using System line, you would have to write System.Console.WriteLine() to print/output text.

- Unlike Java, the name of the C# file does not have to match the class name, but they often do (for better organization). 
  When saving the file, save it using a proper name and add ".cs" to the end of the filename. 


# output
To output values or print text in C#, you can use the : 

1. WriteLine() method:

   Console.WriteLine("Hello World!");
   Console.WriteLine("I am Learning C#");
   Console.WriteLine("It is awesome!");
   Console.WriteLine(3 + 3);


2. Write() method. 
   **This does not insert a new line at the end of the output:
   
   Console.Write("Hello World! ");
   Console.Write("I will print on the same line.");

# comments
Comments can be used to explain C# code, and to make it more readable. It can also be used to prevent execution when testing alternative code.

- Single-line comments start with two forward slashes (//).

- Multi-line comments start with /* and ends with */.

