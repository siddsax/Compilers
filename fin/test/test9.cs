using System;
public class Program
{
    int x = 0;
    int GCD(int num1, int num2)
    {
        int Remainder = 0;
 
        while (num2 > 0 || num2 < 0)
        {
            Remainder = num1 % num2;
            num1 = num2;
            num2 = Remainder;
        }
 
        return num1;
    }
 
     int Main()
    {
        int x, y;
        y = 100;
        x = 125;
        print(GCD(x, y));
    }
}
