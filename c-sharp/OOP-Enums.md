# Enums
An enum is a special "class" that represents a group of constants (unchangeable/read-only variables).

In C#, enums (short for enumerations) are a special type that allows you to define a set of named constants, making your code more readable, type-safe, and maintainable.

# Why And When To Use Enums?
Use enums when you have values that you know aren't going to change, like month days, days, colors, deck of cards, etc.

To create an enum, use the enum keyword (instead of class or interface), and separate the enum items with a comma:

enum Weekday
{
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday,
    Sunday
}

- By default, the underlying type is int.
- The first member starts at 0, and the rest increment by 1 automatically unless specified.

# Assigning Custom Values

enum Status
{
    Pending = 1,
    Approved = 2,
    Rejected = 3,
    Completed = 4
}

Here:
Pending = 1
Approved = 2
Rejected = 3
Completed = 4

# Using Enums in Code
using System;

class Program
{
    enum Status { Pending, Approved, Rejected, Completed }

    static void Main()
    {
        Status currentStatus = Status.Pending;
        Console.WriteLine(currentStatus);          // Output: Pending
        Console.WriteLine((int)currentStatus);     // Output: 0 (the underlying integer value)
    }
}
