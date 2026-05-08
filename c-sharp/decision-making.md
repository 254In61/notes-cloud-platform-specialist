# The if Statement
Use the if statement to specify a block of C# code to be executed if a condition is True.

Syntax

if (condition) 
{
  // block of code to be executed if the condition is True
}

# else
if (condition)
{
  // block of code to be executed if the condition is True
} 
else 
{
  // block of code to be executed if the condition is False
}

# else if
if (condition1)
{
  // block of code to be executed if condition1 is True
} 
else if (condition2) 
{
  // block of code to be executed if the condition1 is false and condition2 is True
} 
else
{
  // block of code to be executed if the condition1 is false and condition2 is False
}

# Short Hand If...Else (Ternary Operator)
There is also a short-hand if else, which is known as the ternary operator because it consists of three operands. 

It can be used to replace multiple lines of code with a single line. 

It is often used to replace simple if else statements:

Syntax : 

variable = (condition) ? expressionTrue :  expressionFalse;

Example : 

int time = 20;

if (time < 18) 
{
  Console.WriteLine("Good day.");
} 
else 
{
  Console.WriteLine("Good evening.");
}


Can be replaced by : 

int time = 20;

string result = (time < 18) ? "Good day." : "Good evening.";

Console.WriteLine(result);

# Switch
Use the switch statement to select one of many code blocks to be executed.

Syntax : 

switch(expression) 
{
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
    break;
}

This is how it works:

- The switch expression is evaluated once
- The value of the expression is compared with the values of each case
- If there is a match, the associated block of code is executed

## break
When C# reaches a break keyword, it breaks out of the switch block.

This will stop the execution of more code and case testing inside the block.

When a match is found, and the job is done, it's time for a break. There is no need for more testing.

A break can save a lot of execution time because it "ignores" the execution of all the rest of the code in the switch block.

# default
The default keyword is optional and specifies some code to run if there is no case match.

Example : 

int day = 4;
switch (day) 
{
  case 6:
    Console.WriteLine("Today is Saturday.");
    break;
  case 7:
    Console.WriteLine("Today is Sunday.");
    break;
  default:
    Console.WriteLine("Looking forward to the Weekend.");
    break;
}
// Outputs "Looking forward to the Weekend."