<h1>Handbook on Programming in C# </h1>

**AP Computer Science Principles 2023-2024**

Husam El-Khatib

<!-- This is a comment (which will not be displayed in the live file);
replace all "???" with your own text. -->




___





<h1>Table of Contents</h1>

- [1. Compiling and Running](#1-compiling-and-running)
- [2. Data Types](#2-data-types)
- [3. Console I/O](#3-console-io)
- [4. Arithmetic Operations](#4-arithmetic-operations)
- [5. Assignment Operations](#5-assignment-operations)
- [6. Comments](#6-comments)
- [7. Decision Structures](#7-decision-structures)
- [8. Conditional Operators](#8-conditional-operators)
- [9. Logic Operators](#9-logic-operators)
- [10. Advanced Decision Structures](#10-advanced-decision-structures)
- [11. String Methods](#11-string-methods)
- [12. Random Generation](#12-random-generation)
- [13. Looping Structures](#13-looping-structures)
- [14. Functions/Methods](#14-functionsmethods)
- [15. Elementary Data Structures](#15-elementary-data-structures)
  - [15.1 Arrays/Lists](#151-arrayslists)
  - [15.2 Matrices](#152-matrices)
- [References](#references)

<!-- 
- [16. Major Keywords](#16-major-keywords)
- [17. Error Handling](#17-error-handling)
- [18. Working with Files](#18-working-with-files)
- [19. Major Language Features](#19-major-language-features)
  - [19.1 Classes](#191-classes)
  - [19.2 Inheritance](#192-inheritance)
  - [19.3 Generic Typing (Templates)](#193-generic-typing-templates)
  - [19.4 Pointers](#194-pointers)
- [20. Importing Local Libraries](#20-importing-local-libraries)
- [21. Working with Time](#21-working-with-time)
- [22. Importing Libaries from Package managers](#22-importing-libaries-from-package-managers)
- [23. Bitwise Operators](#23-bitwise-operators)
- [24. Common Data Structures](#24-common-data-structures)
- [25. Advanced Language Features](#25-advanced-language-features)
-->




___





# 1. Compiling and Running

Compiling and running a C# program involves several steps that allow you to change your source code into an executable application.  In this section, I will go through the process of compiling and running C# programs.

## 1.1 Compiling a C# Program

To compile a C# program, you need access to the C# compiler, which is part of the .NET Framework.  Here's how you can compile a C# program using the command line:

1. ### Open a Command Prompt or Terminal:
   Depending on your operating system, open a command prompt or terminal window.
2. ### Navigate to the Program Directory:
   Use the cd command to navigate to the directory where your C# source file (with a .cs extension) is located.
3. ### Compile the Program:
   Run the following command to compile your program:
  ```cs
  csc YourProgram.cs
  
  ```
  Replace `YourProgram.cs` with the name of your C# source file. This command uses the C# compiler (`csc`) to generate an executable file.
    
4. ### Run the Program:
   After successful compilation, you will see an executable file named `YourProgram.exe` in the same directory. You can run your program using the following command:
  ```cs
  YourProgram.exe

  ```
  Replace `YourProgram.exe` with the name of your executable file.

## 1.2 Understanding Compilation Errors

During compilation, the C# compiler checks your code for syntax errors and other issues. If any errors are found, they will be displayed in the command prompt, along with information about the location of the error in your code. It is essential to review and fix these errors before running your program.

## 1.3 Running a C# Program

Once your program is successfully compiled, you can execute it by running the generated executable file. When you run your program, it starts executing from the Main method, which serves as the entry point.

Here's a simple example of a C# program:
```cs
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, C#!");
    }
}

```
After compiling this program, you can run it to see the output.

## 1.4 IDEs (Integrated Development Environments)

While using the command line for compilation and execution is a fundamental approach, many developers prefer using integrated development environments (IDEs) such as Visual Studio, Visual Studio Code, or JetBrains Rider. These IDEs offer powerful features for C# development, including code editing, debugging, and project management.

In summary, understanding how to compile and run C# programs from the command line is essential for basic development. As you progress in your C# journey, you may explore the features of IDEs to enhance your development experience.





# 2. Data Types

Data types in C# are essential for defining the kind of data that variables can hold. C# provides a rich set of built-in data types, each designed to store specific types of information. Understanding data types is fundamental to writing C# programs effectively.

## 2.1 Common Data Types

### 2.1.1 `int`: Integer
The `int` data type is used to store signed 32-bit integer values. It can represent both positive and negative whole numbers.

Example:
```cs
int age = 25;

```
### 2.1.2 `double`: Double-Precision Floating-Point
The `double` data type is used to store double-precision floating-point numbers, which are decimal numbers with high precision.

Example:
```cs
double pi = 3.14159265359;

```
### 2.1.3 `string`: String
The `string` data type is used to store sequences of characters, such as text. Strings are enclosed in double quotes.

Example:
```cs
string greeting = "Hello, World!";

```
### 2.1.4 `bool`: Boolean
The `bool` data type represents Boolean values, which can be either `true` or `false`. Booleans are used for logical operations and conditional statements.

Example:
```cs
bool isRaining = true;

```
### 2.1.5 `char`: Character
The `char` data type is used to store a single Unicode character. Characters are enclosed in single quotes.

Example:
```cs
char grade = 'A';

```
### 2.1.6 `decimal`: Decimal
The `decimal` data type is used to store decimal numbers with high precision. It is often used in financial calculations where accuracy is crucial.

Example:
```cs
decimal price = 19.99m;

```
### 2.1.7 `byte`: Byte
The `byte` data type is used to store unsigned 8-bit integer values, ranging from 0 to 255.

Example:
```cs
byte redValue = 255;

```
## 2.2 Declaring Variables
To declare a variable, you specify the data type followed by the variable name. Variables can hold data of the declared type.

Example:
```cs
int numberOfApples;
string playerName;
double temperature;

```
## 2.3 Type Inference (`var` Keyword)
C# allows type inference using the `var` keyword. The compiler determines the data type based on the assigned value.

Example:
```cs
var itemCount = 10; // Compiler infers that itemCount is of type int

```
## 2.4 Summary
Understanding and choosing the appropriate data types is essential for efficient and error-free C# programming. C# provides a range of data types to accommodate various types of data, from integers and floating-point numbers to text and Boolean values.






# 3. Console I/O
## 3.1 Introduction to the Console Class
### 3.1.1 What is the Console Class?

The Console class, part of the System namespace, is integral to the .NET framework and provides functionality to read from and write to the console - a text-based user interface. In a console application, which is a command-line based utility, the Console class is the primary way to interact with the user.

### 3.1.2 Using the Console Class

The Console class cannot be instantiated (i.e., you can't create a new object of type Console) because all its members are static. This means you can use these members directly with the class name.

Example:
```cs
Console.Write("Hello ");
Console.WriteLine("World!");

```

The above lines will output **'Hello World!'** with **'WriteLine()'** adding a new line at the end.

Example:
```cs
    Console.Write("Enter your name: ");
    string name = Console.ReadLine();
    Console.WriteLine($"Hello, {name}!");
    
```

    This snippet will prompt the user to enter their name and then greet them.

## 3.2 Writing to the Console
### 3.2.1 Displaying Text

The primary methods for outputting text to the console are **'Console.Write()'** and **'Console.WriteLine()'**. The **'Write()'** method outputs text exactly as provided, while **'WriteLine()'** appends a new line character at the end, moving the cursor to the next line.

### 3.2.2 Formatting Output

Formatted output can be achieved using string interpolation or string formatting. This is useful for creating readable and formatted text, especially with variable data.

    String Interpolation:
```cs
int age = 30;
Console.WriteLine($"You are {age} years old.");

```

String Formatting:
```cs
    float pi = 3.14159f;
    Console.WriteLine("Pi is {0:F2}", pi);
    
```

    This will display **'Pi is 3.14'**, with **'F2'** specifying the floating-point format with two decimal places.

## 3.3 Reading from the Console
### 3.3.1 Reading a String

**'Console.ReadLine()'** reads the next line of characters from the input stream, returning them as a single string. This method is blocking; it pauses program execution until the Enter key is pressed.

### 3.3.2 Reading Characters and Keys

For reading a single key press, including special keys, **'Console.ReadKey()'** is used. It returns a **'ConsoleKeyInfo'** object which has information about the key pressed.

    Example:
```cs
    ConsoleKeyInfo keyInfo = Console.ReadKey();
    Console.WriteLine($"Key pressed: {keyInfo.Key}");

```

## 3.4 Parsing and Converting Input
### 3.4.1 Converting Strings to Numbers

User input is typically read as a string. To use this as a numerical value, you need to convert or parse it. Parsing methods are available for different numeric types.

    Parsing Example:
```cs
    Console.Write("Enter a number: ");
    string input = Console.ReadLine();
    int number;
    if (int.TryParse(input, out number)) {
        Console.WriteLine($"You entered {number}");
    } else {
        Console.WriteLine("That's not a valid number!");
    }

```

### 3.4.2 Error Handling with Input

Exception handling is key when parsing user input to manage unexpected inputs gracefully.

    Try-Catch Example:
```cs
    try {
        Console.Write("Enter another number: ");
        int anotherNumber = int.Parse(Console.ReadLine());
        Console.WriteLine($"Number entered: {anotherNumber}");
    } catch (FormatException) {
        Console.WriteLine("Format Exception: Please enter a correct number!");
    }

```

## 3.5 Best Practices and Common Mistakes
### 3.5.1 Input Validation

Always validate user inputs to protect your program from unexpected or erroneous data. This includes checking for null, verifying the input length, and ensuring it matches the expected format or range.

### 3.5.2 Console I/O in Multithreaded Applications

In a multithreaded environment, it's essential to ensure that console reads and writes are thread-safe to avoid issues like race conditions. Using thread synchronization techniques, such as locks, can help manage this.

    Thread Safety Example:
```cs
    lock(consoleLock) {
        Console.WriteLine("Thread-safe console access");
    }

```

## 3.6 Summary

In this chapter, we've explored the fundamentals of Console I/O in C#. From writing simple messages to the console to parsing complex user inputs and ensuring error handling and thread safety, these skills form the bedrock of creating interactive console applications in C#.






# 4. Arithmetic Operations
## 4.1 Introduction to Arithmetic in C#
### 4.1.1 Understanding Arithmetic Operators

Arithmetic operators in C# are used to perform common mathematical operations such as addition, subtraction, multiplication, and division. These operations are fundamental to almost every aspect of programming, from basic calculations to complex algorithms.

## 4.2 Basic Arithmetic Operators
### 4.2.1 Addition (+)

The **+** operator is used to add two numbers together.
```cs
int sum = 5 + 3; // sum equals 8

```

### 4.2.2 Subtraction (-)

The **-** operator is used to subtract one number from another.
```cs
int difference = 5 - 3; // difference equals 2

```

### 4.2.3 Multiplication (*)

The ***** operator multiplies two numbers.
```cs
int product = 5 * 3; // product equals 15

```

### 4.2.4 Division (/)

The **/** operator divides one number by another. It's important to remember that dividing by zero will result in a runtime error.
```cs
int quotient = 15 / 3; // quotient equals 5

```

### 4.2.5 Modulus (%)

The **%** operator, also known as the modulus or remainder operator, divides one number by another and returns the remainder.
```cs
int remainder = 5 % 3; // remainder equals 2

```

## 4.3 Working with Arithmetic Operators
### 4.3.1 Operator Precedence and Associativity

Understanding the order in which operations are performed (known as operator precedence) and how operators of the same precedence are grouped (associativity) is crucial. For example, multiplication and division have higher precedence than addition and subtraction.
```cs
int result = 5 + 3 * 2; // result equals 11, not 16

```

### 4.3.2 Using Parentheses to Control Order of Operations

Parentheses **()** can be used to explicitly define the order of operations, overriding the default precedence rules.
```cs
int result = (5 + 3) * 2; // result equals 16

```

## 4.4 Advanced Concepts
### 4.4.1 Integer Division and Floating-Point Division

In C#, the result of a division operation varies depending on the data type of the numbers involved. If both numbers are integers, the result is an integer (fractional part is discarded). To get a fractional result, at least one of the operands must be a floating-point type (e.g., **float**, **double**).
```cs
int intDiv = 7 / 3;       // Result is 2
double floatDiv = 7 / 3.0; // Result is 2.33333...

```

### 4.4.2 Compound Assignment Operators

Compound assignment operators combine an arithmetic operation with assignment. For example, **x += y** is equivalent to **x = x + y**.
```cs
int x = 5;
x += 3; // x is now 8

```

## 4.5 Practical Examples
### 4.5.1 Calculating the Area of a Circle

Demonstrate the use of multiplication and the **Math** library's **PI** constant to calculate the area of a circle given its radius.
```cs
double radius = 5.0;
double area = Math.PI * radius * radius;
Console.WriteLine($"The area of the circle is: {area}");

```

### 4.5.2 Converting Fahrenheit to Celsius

Use arithmetic operations to convert a temperature from Fahrenheit to Celsius.
```cs
double fahrenheit = 68;
double celsius = (fahrenheit - 32) * 5 / 9;
Console.WriteLine($"{fahrenheit}°F is equal to {celsius}°C");

```

## 4.6 Summary

This chapter covered the fundamental arithmetic operations in C#, illustrating how they are used in different contexts, the importance of operator precedence, and practical applications in everyday programming tasks.






# 5. Assignment Operations







___





# 6. Comments

???





___





# 7. Decision Structures

???





___





# 8. Conditional Operators

???





___





# 9. Logic Operators

???





___





# 10. Advanced Decision Structures

???





___





# 11. String Methods

???





___





# 12. Random Generation

???





___





# 13. Looping Structures

???





___





# 14. Functions/Methods

???





___





# 15. Elementary Data Structures

???





## 15.1 Arrays/Lists

???






## 15.2 Matrices

???





___





<!-- 
EVERYTHING BELOW IS OPTIONAL; 
UNCOMMENT BY REMOVING THE ARROW TAGS SURROUNDING
(i.e., delete the "< !--" and "-- >" tags)

CHANGE THE SECTION NUMBERS AS DESIRED
-->

<!-- # 16. Major Keywords

???





___ -->





<!-- # 17. Error Handling

???





___ -->





<!-- # 18. Working with Files

???





___ -->





<!-- # 19. Major Language Features

???







## 19.1 Classes

???





## 19.2 Inheritance

???





## 19.3 Generic Typing (Templates)

???





## 19.4 Pointers

???





___ -->





<!-- # 20. Importing Local Libraries

???





___ -->





<!-- # 21. Working with Time

???





___ -->





<!-- # 22. Importing Libaries from Package managers

???





___ -->





<!-- # 23. Bitwise Operators

???





___ -->





<!-- # 24. Common Data Structures

???





___ -->





<!-- # 25. Advanced Language Features

???





___ -->





# References

* [Markdown Cheatsheet](https://gist.github.com/jonschlinkert/5854601)
* [description](http://example.com)
