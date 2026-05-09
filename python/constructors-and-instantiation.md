# Intro

https://realpython.com/python-class-constructor/

- Python supports OOP.At the heart of Python’s object-oriented capabilities, you’ll find the 'class' keyword, 
  which allows you to define custom classes that can have attributes for storing data and methods for providing behaviors.

- Once you have a class to work with, then you can start creating new instances or objects of that class,
  which is an efficient way to reuse functionality in your code.

- Creating and initializing objects of a given class is a fundamental step in object-oriented programming. 
  This step is often referred to as object construction or instantiation. 
  The tool responsible for running this instantiation process is commonly known as a class constructor.


# Python’s Instantiation Process

- Whenever you call a Python class to create a new instance, you trigger python instantiation process.
- The Python’s instantiation process runs through two separate steps :
  1. a call to the class constructor, which triggers the instance creator, .__new__(), to create a new empty object. 
  2. initialize the newly created object with the instance initializer, .__init__(), which takes the constructor’s arguments 

"""
- Sample code to undestand the concept of constructors
"""

class Calculator:

    '''
    defines the .__new__() method, which takes the class as its first argument. 

    Note that using cls as the name of this argument is a strong convention 
    in Python, just like using self to name the current instance is. 

    The method also takes *args and **kwargs, which allow for passing an 
    undefined number of initialization arguments to the underlying instance.
    '''
    def __new__(cls, *args, **kwargs):
        print("Step 1 : Ceating a new instance of Calculator")
        return super().__new__(cls)
    
    def __init__(self, number_one, number_two):
        print("Step 2 : Initialize the new instance of Calculator")
        self.number_one = number_one
        self.number_two = number_two

    def add(self):
        return f"{self.number_one} + {self.number_two} = {self.number_one + self.number_two}"
    
    def subtract(self):
        return f"{self.number_one} - {self.number_two} = {self.number_one - self.number_two}"
    

def main():
    - Create a new instance of Calculator class, by calling the class with 
    a pair of parentheses.


    - When you call a class like the above example, you’re calling the class 
      constructor.
      This class constructor creates, initializes, and returns a new object 
      by triggering Python’s internal instantiation process.
    
    - Calling a class creates as instance of the class. This is NOT the same 
      as calling an instance of a class. 

      These are two different and unrelated topics. 
      To make a class’s instance callable, you need to implement a 
      .__call__() special method, which has nothing to do with Python’s instantiation process.


    calc = Calculator(14,6)
    print(calc.add())
    print(calc.subtract())
    

if __name__ == "__main__":
    main()