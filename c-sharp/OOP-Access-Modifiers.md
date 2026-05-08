# modifiers
C# has the following access modifiers:

1. public: The code is accessible for all classes

2. private: The code is only accessible within the same class
   Trying to access a fiel from outside the class you'll get errors like : 
   "'Car.model' is inaccessible due to its protection level
    The field 'Car.model' is assigned but its value is never used"

   By default, all members of a class are private if you don't specify an access modifier

3. protected: The code is accessible within the same class, or in a class that is inherited from that class.
4. internal: The code is only accessible within its own assembly, but not from another assembly. 

There's also two combinations: protected internal and private protected.

# Why Access Modifiers?
To control the visibility of class members (the security level of each individual class and class member).

To achieve "Encapsulation" - which is the process of making sure that "sensitive" data is hidden from users. This is done by declaring fields as private.

