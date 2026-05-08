# overview

Console.WriteLine() is used to output (print) values. 

Console.ReadLine() to get user input.

// Type your username and press enter
Console.WriteLine("Enter username:");

// Create a string variable and get user input from the keyboard and store it in the variable
string userName = Console.ReadLine();

// Print the value of the variable (userName), which will display the input value
Console.WriteLine("Username is: " + userName);

# User Input and Numbers
The Console.ReadLine() method returns a string. Therefore, you cannot get information from another data type, such as int. 

The following program will cause an error:

Example
Console.WriteLine("Enter your age:");
int age = Console.ReadLine();
Console.WriteLine("Your age is: " + age);

The error message will be something like this:

"Cannot implicitly convert type 'string' to 'int'"

Like the error message says, you cannot implicitly convert type 'string' to 'int'.

It is possible to convert data types explicitly by using built-in methods such as :
1. Convert.ToBoolean
2. Convert.ToDouble
3. Convert.ToString
4. Convert.ToInt32 (int)
5. Convert.ToInt64 (long)

Console.WriteLine("Enter your age:");
int age = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Your age is: " + age);