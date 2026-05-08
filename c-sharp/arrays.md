# overview
Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

To declare an array, define the variable type with square brackets:

string[] cars;

We have now declared a variable that holds an array of strings.

To insert values to it, we can use an array literal - place the values in a comma-separated list, inside curly braces:

string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};


To create an array of integers, you could write:

int[] myNum = {10, 20, 30, 40};

# access elements of an array 
You access an array element by referring to the index number.

string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
Console.WriteLine(cars[0]);
// Outputs Volvo

# change an array element
To change the value of a specific element, refer to the index number:

cars[0] = "Opel";

# Array Length
To find out how many elements an array has, use the Length property:

string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
Console.WriteLine(cars.Length);
// Outputs 4

# Other Ways to Create an Array
In C#, there are different ways to create an array:

// Create an array of four elements, and add values later
string[] cars = new string[4];

// Create an array of four elements and add values right away 
string[] cars = new string[4] {"Volvo", "BMW", "Ford", "Mazda"};

// Create an array of four elements without specifying the size 
string[] cars = new string[] {"Volvo", "BMW", "Ford", "Mazda"};

// Create an array of four elements, omitting the new keyword, and without specifying the size
string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};

It is up to you which option you choose. 

However, you should note that if you declare an array and initialize it later, you have to use the new keyword:

// Declare an array
string[] cars;

// Add values, using new
cars = new string[] {"Volvo", "BMW", "Ford"};

// Add values without using new (this will cause an error)
cars = {"Volvo", "BMW", "Ford"};

# Loop through an Array

for loop
========
You can loop through the array elements with the for loop, and use the Length property to specify how many times the loop should run.

The following example outputs all elements in the cars array:

string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
for (int i = 0; i < cars.Length; i++) 
{
  Console.WriteLine(cars[i]);
}


foreach Loop
==============
There is also a foreach loop, which is used exclusively to loop through elements in an array:

Syntax

foreach (type variableName in arrayName) 
{
  // code block to be executed
}

string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};

foreach (string i in cars) 
{
  Console.WriteLine(i);
}

=> foreach method is easier to write, it does not require a counter (using the Length property), and it is more readable.

# Sort Arrays
There are many array methods available, for example Sort(), which sorts an array alphabetically or in an ascending order:

// Sort a string
string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
Array.Sort(cars);
foreach (string i in cars)
{
  Console.WriteLine(i);
}
 
// Sort an int
int[] myNumbers = {5, 1, 8, 9};
Array.Sort(myNumbers);
foreach (int i in myNumbers)
{
  Console.WriteLine(i);
}

# System.Linq Namespace
Other useful array methods, such as Min, Max, and Sum, can be found in the System.Linq namespace:

using System;
using System.Linq;

namespace MyApplication
{
  class Program
  {
    static void Main(string[] args)
    {
      int[] myNumbers = {5, 1, 8, 9};
      Console.WriteLine(myNumbers.Max());  // returns the largest value
      Console.WriteLine(myNumbers.Min());  // returns the smallest value
      Console.WriteLine(myNumbers.Sum());  // returns the sum of elements
    }
  }
}