/*
 * C# Program to Swap two Numbers
 */
using System;
//test comment
class Test
{
    void Main(string[] args)
    {
        int num1, num2;
        num1 = int.Parse(Console.ReadLine());
        num2 = int.Parse(Console.ReadLine());
        num1 = num1 + num2;
        num2 = num1 - num2;
        num1 = num1 - num2;
    }
}
