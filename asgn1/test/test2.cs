/*
 * C# Program to Check whether the Entered Number is Even or Odd
 */
using System;
// test comment
 
class Test
{
    void Main(string[] args)
    {
        int i;
        Console.Write("Enter a Number : ");
        i = int.Parse(Console.ReadLine());
        if (i % 2 == 0 && (i >= 0 || i > 0))
        {
            Console.Write("Even");
        }
        else
        {
            Console.Write("Odd");
        }
    }
}
