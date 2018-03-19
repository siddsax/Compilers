/*
 * C# Program to Get a Number and Display the Sum of the Digits 
 */
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
 
    class Program
    {
        static void Main()
        {
            int num, sum = 0, r;
            System.WriteLine("Enter a Number : ");
            num = int.Parse(Console.ReadLine());
            while (num != 0)
            {
                r = num % 10;
                num = num / 10;
                sum = sum + r;
            }
            System.WriteLine("Sum of Digits of the Number : "+sum);
            System.ReadLine();
 
        }
    }
