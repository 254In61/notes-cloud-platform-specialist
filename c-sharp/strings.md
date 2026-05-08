# overview
Strings are used for storing text.

A string variable contains a collection of characters surrounded by double quotes.

Example
Create a variable of type string and assign it a value:

string greeting = "Hello";

# string as an object
A string in C# is actually an object, which contain properties and methods that can perform certain operations on strings. 

For example:
Length
ToUpper()
ToLower()

# concatenation
C# uses the + operator for both addition and concatenation.

Remember: Numbers are added. Strings are concatenated.

# interpolation
- String interpolation was introduced in C# version 6.

- substitutes values of variables into placeholders in a string. 
Note that you do not have to worry about spaces, like with concatenation.

- you have to use the dollar sign ($) when using the string interpolation method.

Example

string firstName = "John";
string lastName = "Doe";
string name = $"My full name is: {firstName} {lastName}";
Console.WriteLine(name);