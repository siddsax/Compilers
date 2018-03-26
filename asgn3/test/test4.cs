using System;
using Generic;
using Linq;
using Text;
 
class Program
{
    void Main()
    {
        int num, reverse = 0;
        Console.WriteLine("Enter a Number : ");
        num = Parse(Console.ReadLine());
        while (num != 0)
        {
            reverse = reverse * 10;
            reverse = reverse + num % 10;
            num = num / 10;
        }
        Console.WriteLine("Reverse of Entered Number is : "+reverse);
        Console.ReadLine();

    }
}
