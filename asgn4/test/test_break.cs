using System;
class Test
{
    void Main() 
    {
        int i = 5;
        while (i > 3)
        {
            if (i > 2)
            {
                int c = 3;
                i++;
                c++;
            }
            else
            {
                while (i > 2)
                {
                    break;
                    i++;
                }
            }
        }  
    }
}
