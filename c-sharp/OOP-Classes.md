# Class Members
Fields and methods inside classes are often referred to as "Class Members":

Create a Car class with three class members: two fields and one method.

// The class
class MyClass
{
  // Class members
  string color = "red";        // field
  int maxSpeed = 200;          // field

  public void fullThrottle()   // method
  {
    Console.WriteLine("The car is going as fast as it can!");
  }
}

# Fields
Variables inside a class are called fields.

These variables could be just a declaration or can be instantiated.

class Car 
{
  string model;
  string color = "red";        // instantiated 
  int year;

  static void Main(string[] args)
  {
    Car Ford = new Car();
    Ford.model = "Mustang";
    Ford.color = "red";
    Ford.year = 1969;

    Car Opel = new Car();
    Opel.model = "Astra";
    Opel.color = "white";
    Opel.year = 2005;

    Console.WriteLine(Ford.model);
    Console.WriteLine(Opel.model);
  }
}

You can access them by creating an object of the class and by using the dot syntax(.).
