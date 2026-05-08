# objective
- Split classes into different files and consume them from there.

- In real-world C# projects, we don’t just dump everything in one folder. We organize classes into folders that map to namespaces. That way, your code is modular and scalable as the project grows.

- Enterprise projects go ahead and organize classes into folders & namespaces (like Models/Person.cs, Services/Calculator.cs)

# Example Project Layout

MyApp/
 ├── Program.cs              # entry point
 ├── Models/
 │    └── Person.cs          # data classes (models)
 ├── Services/
 │    └── Calculator.cs      # business logic / services
 └── Utils/
      └── StringHelper.cs    # helper utilities


! Program.cs
using System;
using MyApp.Models;    // Import namespace for Person
using MyApp.Services;  // Import namespace for Calculator
using MyApp.Utils;     // Import namespace for helpers

namespace MyApp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Models
            Person person = new Person("Allan", 43);
            Console.WriteLine(person.GetInfo());

            // Services
            Calculator calc = new Calculator();
            Console.WriteLine($"2 + 3 = {calc.Add(2, 3)}");

            // Utils
            Console.WriteLine(StringHelper.Capitalize("hello from c#"));
        }
    }
}

! Models/Person.cs

namespace MyApp.Models
{
    public class Person
    {
        public string Name { get; }
        public int Age { get; }

        public Person(string name, int age)
        {
            Name = name;
            Age = age;
        }

        public string GetInfo()
        {
            return $"Name: {Name}, Age: {Age}";
        }
    }
}

! Services/Calculator.cs
namespace MyApp.Services
{
    public class Calculator
    {
        public int Add(int a, int b) => a + b;

        public int Multiply(int a, int b) => a * b;
    }
}

! Utils/StringHelper.cs
using System.Globalization;

namespace MyApp.Utils
{
    public static class StringHelper
    {
        public static string Capitalize(string input)
        {
            if (string.IsNullOrWhiteSpace(input)) return input;

            return CultureInfo.CurrentCulture.TextInfo.ToTitleCase(input);
        }
    }
}

# Is Program.cs file a must?
yes and no depending on the kind of C# project you’re building.

1. Console / CLI apps

- Program.cs is required (or at least some file with a Main method).

- The Main method is the entry point of your application (just like int main() in C++ or public static void main in Java).

- By convention, .NET projects put Main in Program.cs.

👉 But technically, the file doesn’t have to be named Program.cs.
You could call it App.cs or EntryPoint.cs — what matters is that it contains Main.

2. ASP.NET Core (Web APIs / Web Apps)

- Since .NET 6, Microsoft introduced top-level statements → you don’t even see Main anymore.

- Instead of a Program.cs with a Main method, you get something like:

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello World!");

app.Run();

- This is still in Program.cs, but the compiler generates the hidden Main for you.

👉 You could merge this into another file, but the default convention is to keep it in Program.cs so devs know where the app starts.

3. Class Libraries (DLLs)

- If you’re writing a class library (e.g., MyLibrary.dll), you don’t need Program.cs or Main.

- A library has no entry point; it’s just a collection of classes that another app consumes.

# Class name matching filename?
- Not all. 

File: Person.cs

namespace MyApp.Models
{
    public class Human   // class name is Human, not Person
    {
        public string Name { get; set; }
    }
}

- This compiles perfectly fine, even though the file is Person.cs and the class is Human.

Best Practice
==============

By convention, C# developers name the file the same as the public class inside it:

- Person.cs → contains public class Person
- Calculator.cs → contains public class Calculator

Why?
- Easier to navigate codebases.
- IDEs like Visual Studio / Rider auto-suggest this.
- Large teams expect it.

NB : The compiler doesn’t care.
But for readability, maintainability, and job-ready code, match class name = file name (1 class per file).