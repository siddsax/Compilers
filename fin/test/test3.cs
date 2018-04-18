/*
 * C# Program to Get a Number and Display the Sum of the Digits 
 */
using System;
using Generic;
using Linq;
using Text;
 
class Program
{
    void Main()
    {
        int num, sum = 0, r;
        // print("Enter a Number : ");
        num = 0;
        while (num != 0)
        {
            r = num % 10;
            num = num / 10;
            sum = sum + r;
        }
        print(sum);

    }
}
