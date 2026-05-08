# intro
Type casting is when you assign a value of one data type to another type.

In C#, there are two types of casting:

# Implicit Casting 
- converting a smaller type to a larger type size
char -> int -> long -> float -> double

- Implicit casting is done automatically when passing a smaller size type to a larger size type

Example

int myInt = 9;
double myDouble = myInt;       // Automatic casting: int to double .. I am promoting an initial int value to a double.

Console.WriteLine(myInt);      // Outputs 9
Console.WriteLine(myDouble);   // Outputs 9

# Explicit Casting

- converting a larger type to a smaller size type
double -> float -> long -> int -> char

- Explicit casting must be done manually by placing the type in parentheses in front of the value

Example

double myDouble = 9.78;
int myInt = (int) myDouble;    // Manual casting: double to int .. Demoting an originally double value to become an int.

Console.WriteLine(myDouble);   // Outputs 9.78
Console.WriteLine(myInt);      // Outputs 9

# Type Conversion Methods
It is also possible to convert data types explicitly by using built-in methods such as :
1. Convert.ToBoolean
2. Convert.ToDouble
3. Convert.ToString
4. Convert.ToInt32 (int)
5. Convert.ToInt64 (long)

Example
int myInt = 10;
double myDouble = 5.25;
bool myBool = true;

Console.WriteLine(Convert.ToString(myInt));    // convert int to string
Console.WriteLine(Convert.ToDouble(myInt));    // convert int to double
Console.WriteLine(Convert.ToInt32(myDouble));  // convert double to int
Console.WriteLine(Convert.ToString(myBool));   // convert bool to string