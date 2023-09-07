using System;



   
    double pi = 3.14159;

    Console.WriteLine("Enter the radius");
    double rad = Convert.ToDouble(Console.ReadLine());
    double area = pi * rad * rad;
    double circ = 2 * pi * rad;

    Console.WriteLine("The radius is: " + rad);
    Console.WriteLine("The area is: " + area);
    Console.WriteLine("The circumference is: " + circ);
