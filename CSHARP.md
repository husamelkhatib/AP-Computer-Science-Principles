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

Console Input and Output (I/O) is a fundamental aspect of C# programming. It allows you to interact with the user by reading input from the console and displaying output.

## 3.1 Output with `Console.WriteLine()`

The `Console.WriteLine()` method is used to display output to the console. It automatically adds a newline character at the end of the output, so each call starts on a new line.

Example:
```cs
Console.WriteLine("Hello, C#!");

```
Output:
```cs
Hello, C#!

```
## 3.2 Input with `Console.ReadLine()`

The `Console.ReadLine()` method is used to read input from the user. It allows the user to enter text, which is returned as a string.

Example:
```cs
Console.WriteLine("Enter your name:");
string name = Console.ReadLine();
Console.WriteLine("Hello, " + name + "!");

```
In this example, the program prompts the user to enter their name and then greets them using the provided name.

## 3.3 Formatting Output

You can format output using placeholders and string interpolation. Placeholders are indicated by `{0}`, `{1}`, etc., and values are substituted accordingly.

Example:
```cs
string name = "Alice";
int age = 30;
Console.WriteLine("Name: {0}, Age: {1}", name, age);

```
Output:
```cs
Name: Alice, Age: 30

```
Alternatively, you can use string interpolation with the `$` symbol:
```cs
Console.WriteLine($"Name: {name}, Age: {age}");

```

## 3.4 Reading Numeric Input

When you read input using `Console.ReadLine()`, it's returned as a string. To work with numeric values, you need to parse the string into the desired data type using methods like `int.Parse()` or `double.Parse()`.

Example:
```cs
Console.WriteLine("Enter your age:");
string ageInput = Console.ReadLine();
int age = int.Parse(ageInput);
Console.WriteLine("You entered: " + age);

```
Ensure error handling when parsing input to handle cases where the input cannot be converted to the desired data type.

## 3.5 Summary

Console I/O is a critical part of C# programming, enabling you to communicate with users by displaying information and collecting input. Understanding how to use `Console.WriteLine()` for output and `Console.ReadLine()` for input is essential for building interactive C# applications.






# 4. Arithmetic Operations

Arithmetic operations are fundamental in C# and allow you to perform mathematical calculations on numeric data types. C# supports a variety of arithmetic operations, including addition, subtraction, multiplication, division, and more.

## 4.1 Basic Arithmetic Operators
### 4.1.1 Addition (`+`)

The addition operator `+` is used to add two or more numeric values.

Example:
```cs
int a = 5;
int b = 3;
int sum = a + b; // sum is 8

```
### 4.1.2 Subtraction (`-`)

The subtraction operator `-` is used to subtract one numeric value from another.

Example:
```cs
int x = 10;
int y = 4;
int difference = x - y; // difference is 6

```
### 4.1.3 Multiplication (`*`)

The multiplication operator `*` is used to multiply two or more numeric values.

Example:
```cs
int p = 6;
int q = 7;
int product = p * q; // product is 42

```
### 4.1.4 Division (`/`)

The division operator `/` is used to divide one numeric value by another. Note that division of integers may result in a truncated integer value.

Example:
```cs
double dividend = 10.0;
double divisor = 3.0;
double quotient = dividend / divisor; // quotient is 3.333...

```
## 4.2 Modulus Operator (`%`)

The modulus operator `%` calculates the remainder when one number is divided by another. It is often used to check if a number is even or odd.

Example:
```cs
int num = 7;
int remainder = num % 2; // remainder is 1 (7 is odd)

```
## 4.3 Order of Operations

C# follows the standard order of operations (PEMDAS/BODMAS), which determines the sequence in which arithmetic operations are evaluated:

  1. **P**arentheses (Brackets)
  2. **E**xponents (Powers and Roots)
  3. **M**ultiplication and **D**ivision (left to right)
  4. **A**ddition and **S**ubtraction (left to right)

Use parentheses to control the order of evaluation when needed.

## 4.4 Summary

Understanding arithmetic operations is crucial for performing mathematical calculations in C# programs. By using basic arithmetic operators like addition, subtraction, multiplication, and division, you can manipulate numeric data and solve a wide range of problems.






# 5. Assignment Operations

???





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
