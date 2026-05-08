# overview
Variables are containers for storing data values.

In C#, there are different types of variables (defined with different keywords), for example:

1. int - stores integers (whole numbers), without decimals, such as 123 or -123
2. double - stores floating point numbers, with decimals, such as 19.99 or -19.99
3. char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes
4. string - stores text, such as "Hello World". String values are surrounded by double quotes
5. bool - stores values with two states: true or false

# declare variables
type variableName = value;

Where type is a C# type (such as int or string), and variableName is the name of the variable (such as x or name). 

Create a variable called name of type string and assign it the value "John":

string name = "John";
Console.WriteLine(name);

Create a variable called myNum of type int and assign it the value 15:

int myNum = 15;
Console.WriteLine(myNum);

ou can also declare a variable without assigning the value, and assign the value later:

int myNum;
myNum = 15;
Console.WriteLine(myNum);


A demonstration of how to declare variables of other types:

int myNum = 5;
double myDoubleNum = 5.99D;
char myLetter = 'D';
bool myBool = true;
string myText = "Hello";

# constants
If you don't want others (or yourself) to overwrite existing values, you can add the const keyword in front of the variable type.

This will declare the variable as "constant", which means unchangeable and read-only:

const int myNum = 15;
myNum = 20; // error

Note: You cannot declare a constant variable without assigning the value. If you do, an error will occur.

# Display Variables
The WriteLine() method is often used to display variable values to the console window.

string name = "John";
Console.WriteLine("Hello " + name);

string firstName = "John ";
string lastName = "Doe";
string fullName = firstName + lastName;
Console.WriteLine(fullName);


For numeric values, the + character works as a mathematical operator (notice that we use int (integer) variables here):
int x = 5;
int y = 6;
Console.WriteLine(x + y); // Print the value of x + y

From the example above, you can expect:

x stores the value 5
y stores the value 6
Then we use the WriteLine() method to display the value of x + y, which is 11

# Multiple Variables
To declare more than one variable of the same type, use a comma-separated list:

int x = 5, y = 6, z = 50;
Console.WriteLine(x + y + z);

You can also assign the same value to multiple variables in one line:

int x, y, z;
x = y = z = 50;
Console.WriteLine(x + y + z);

# Identifiers

All C# variables must be identified with unique names.
These unique names are called identifiers.

Identifiers can be short names (like x and y) or more descriptive names (age, sum, totalVolume).

Note: It is recommended to use descriptive names in order to create understandable and maintainable code:

// Good
int minutesPerHour = 60;

// OK, but not so easy to understand what m actually is
int m = 60;

The general rules for naming variables are:
- Names can contain letters, digits and the underscore character (_)
- Names must begin with a letter or underscore
- Names should start with a lowercase letter, and cannot contain whitespace
- Names are case-sensitive ("myVar" and "myvar" are different variables)
- Reserved words (like C# keywords, such as int or double) cannot be used as names