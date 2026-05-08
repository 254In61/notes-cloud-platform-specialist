# overview
An exception is defined as an event that occurs during the execution of a program that is unexpected by the program code. 
The actions to be performed in case of occurrence of an exception is not known to the program. 

In such a case, we create an exception object and call the exception handler code. 
The execution of an exception handler so that the program code does not crash is called exception handling. 
Exception handling is important because it gracefully handles an unwanted event, an exception so that the program code still makes sense to the user.

# syntax

- try	   : Used to define a try block. This block holds the code that may throw an exception.
- catch	   : Used to define a catch block. This block catches the exception thrown by the try block.
- finally  : Used to define the finally block. This block holds the default code.
             The finally block is the part of the code that has to be executed irrespective of if the exception was generated or not.
- throw    : Used to throw an exception manually.

Example: 
        try
        {
            for (int i = 0; i < 9; i++)
            {
                Console.WriteLine(arr_x[i]);
            }
        }

        catch (IndexOutOfRangeException e)
        {
            /* 
            The Message property of the object of type IndexOutOfRangeException
            is used to display the type of exception that has occurred to the user.
            */
            Console.WriteLine("An Exception has occurred : {0}", e.Message);
        }

        finally
        {
            Console.WriteLine("\nThis is the finally block. \nI have to be executed irrespective of exeception generated or not");
        }

# Using Multiple try-catch blocks

Multiple catch blocks are used when we are not sure about the exception type that may be generated, so we write different blocks to tackle any type of exception that is encountered. 

The finally block is the part of the code that has to be executed irrespective of if the exception was generated or not. 


# User Defined Exceptions

User-defined exceptions are useful when we want to code an exception that may not be defined by the language. 

For example, in a boiler room, if the temperature rises above some threshold then the heat must be turned off. 

For understanding how user-defined exceptions are used we take an example of a division by zero. Here we define a class DivByZero that inherits from Exception and is called by the DivisionOperation function when the denominator is equal to zero. 

Since the call for the function is may or may not throw an exception it is placed in the try block. A catch block is defined to catch any exception of type Exception and the Message property prints the type of exception that has occurred.

