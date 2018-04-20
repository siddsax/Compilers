class bubblesort
{
       void Main(string[] args)
       {
           int[] a = new int[5];
           a[0]=1;
           a[1]=10;
           a[2]=4;
           a[3]=8;
           a[4]=-98;
           // int[] a = { 3, 2, 5, 4, 1 };  
           int t = 0;
           // Console.WriteLine("The Array is : ");
           while(t<5){
               print(a[t]);
               t++;
           }
           t =0;
           int i,j;
           i=0;
           j=0;
           while(j<5-2)
           // for (int j = 0; j <= a.Length - 2; j++)
           {
               i=0;
               // for (int i = 0; i <= a.Length - 2; i++)
               while(i<=5-2)
               {
                   if (a[i] > a[i + 1])
                   {
                       t = a[i + 1];
                       a[i + 1] = a[i];
                       a[i] = t;
                   }
               i++;
               }
           j++;
           }
           // Console.WriteLine("The Sorted Array :");
           t=0;
           while(t<5){
               print(a[t]);
               t++;
           }
        }

    }