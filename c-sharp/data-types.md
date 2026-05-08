# overview
int	    4 bytes	Stores whole numbers from -2,147,483,648 to 2,147,483,647
long	8 bytes	Stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
float	4 bytes	Stores fractional numbers. Sufficient for storing 6 to 7 decimal digits
double	8 bytes	Stores fractional numbers. Sufficient for storing 15 decimal digits
bool	1 byte	Stores true or false values
char	2 bytes	Stores a single character/letter, surrounded by single quotes
string	2 bytes per character	Stores a sequence of characters, surrounded by double quotes

# Numbers
Number types are divided into two groups:

1. Integer types 
- stores whole numbers, positive or negative (such as 123 or -456), WITHOUT decimals. 
- Valid types are int and long. Which type you should use, depends on the numeric value.

int myNum = 100000;
Console.WriteLine(myNum);

long myNum = 15000000000L;
Console.WriteLine(myNum);


2. Floating point types represents numbers with a fractional part, containing one or more decimals. 
- Valid types are float and double.

- You should use a floating point type whenever you need a number with a decimal, such as 9.99 or 3.14515.
- The float and double data types can store fractional numbers. 
- Note that you should end the value with an "F" for floats and "D" for doubles.

float myNum = 5.75F;
Console.WriteLine(myNum);

double myNum = 19.99D;
Console.WriteLine(myNum);

A floating point number can also be a scientific number with an "e" to indicate the power of 10:

float f1 = 35e3F;
double d1 = 12E4D;
Console.WriteLine(f1);
Console.WriteLine(d1);


Even though there are many numeric types in C#, the most used for numbers are int (for whole numbers) and double (for floating point numbers).
he precision of a floating point value indicates how many digits the value can have after the decimal point. 
The precision of float is only six or seven decimal digits, while double variables have a precision of about 15 digits. Therefore it is safer to use double for most calculations.

# Boolean
A boolean data type is declared with the bool keyword and can only take the values true or false.
Boolean values are mostly used for conditional testing.

bool isCSharpFun = true;
bool isFishTasty = false;
Console.WriteLine(isCSharpFun);   // Outputs True
Console.WriteLine(isFishTasty);   // Outputs False

# Characters
The char data type is used to store a single character. 
The character must be surrounded by single quotes, like 'A' or 'c':

char myGrade = 'B';
Console.WriteLine(myGrade);

# Strings
The string data type is used to store a sequence of characters (text). 
String values must be surrounded by double quotes.

string greeting = "Hello World";
Console.WriteLine(greeting);

