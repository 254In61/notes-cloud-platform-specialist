# Data Abstraction
Data abstraction is the process of hiding certain details and showing only essential information to the user.

Abstraction can be achieved with either abstract classes or interfaces.

The abstract keyword is used for classes and methods:

- Abstract class: is a restricted class that cannot be used to create objects (to access it, it must be inherited from another class).

- Abstract method: can only be used in an abstract class, and it does not have a body. The body is provided by the derived class (inherited from).

An abstract class can have both abstract and regular methods:

// Abstract class
abstract class Animal
{
  // Abstract method (does not have a body)
  public abstract void animalSound();

  // Regular method
  public void sleep()
  {
    Console.WriteLine("Zzz");
  }
}

// To access the abstract class, it must be inherited from another class. 

// Derived class (inherit from Animal)
class Pig : Animal
{
  public override void animalSound()
  {
    // The body of animalSound() is provided here
    Console.WriteLine("The pig says: wee wee");
  }
}

// Derived class (inherit from Animal)
class Dog : Animal
{
  public override void animalSound()
  {
    Console.WriteLine("The dog says: bow wow");
  }
}

class Program
{
  static void Main(string[] args)
  {
    Pig myPig = new Pig(); // Create a Pig object
    myPig.animalSound();  // Call the abstract method
    myPig.sleep();  // Call the regular method

    Dog myDog = new Dog(); // Create a Dog object
    myDog.animalSound();  // Call the abstract method
    myDog.sleep();  // Call the regular method
  }
}

