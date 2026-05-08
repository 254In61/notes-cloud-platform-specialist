# Why OOP? Prodecural programing?
OOP stands for Object-Oriented Programming.

Procedural programming is about writing procedures or methods that perform operations on the data, while object-oriented programming is about creating objects that contain both data and methods.

Object-oriented programming has several advantages over procedural programming:

- OOP is faster and easier to execute
- OOP provides a clear structure for the programs
- OOP helps to keep the C# code DRY "Don't Repeat Yourself", and makes the code easier to maintain, modify and debug
- OOP makes it possible to create full reusable applications with less code and shorter development time

Tip: The "Don't Repeat Yourself" (DRY) principle is about reducing the repetition of code. 
You should extract out the codes that are common for the application, and place them at a single place and reuse them instead of repeating it.

# Classes vs Objects .. and Attributes vs Methods
A class is a template for objects. It is an object constructor, or a "blueprint" for creatin objects.

An object is an instance of a class.
When the individual object are created, they inherit all the variables and methods from the class.

Class = Fruit
objects = Apple, Banana, Mango

Everything in C# is associated with classes and objects, along with its attributes and methods. 

For example: in real life, a car is an object. The car has attributes, such as weight and color, and methods, such as drive and brake.

Methods normally belong to a class, and they define how an object of a class behaves.

# creating a class
class Car 
{
  string color = "red"; 

}

- When a variable is declared directly in a class, it is often referred to as a field (or attribute).

- It is not required, but it is a good practice to start with an uppercase first letter when naming classes. 

- Also, it is common that the name of the C# file and the class matches, as it makes our code organized. However it is not required (like in Java).

# create an object
An object is created from a class. We have already created the class named Car, so now we can use this to create objects.

To create an object of Car, specify the class name, followed by the object name, and use the keyword "new":

class Car 
{
  string color = "red";

  static void Main(string[] args)
  {
    Car myObj1 = new Car();
    Car myObj2 = new Car();
    Console.WriteLine(myObj1.color);
    Console.WriteLine(myObj2.color);
  }
}

# multiple classes
You can also create an object of a class and access it in another class. This is often used for better organization of classes (one class has all the fields and methods, while the other class holds the Main() method (code to be executed)).


!prog2.cs
class Car 
{
  public string color = "red";
}

!prog.cs
class Program
{
  static void Main(string[] args)
  {
    Car myObj = new Car();
    Console.WriteLine(myObj.color);
  }
}
