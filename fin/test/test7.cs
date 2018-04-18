using System;
public class goal
{
    int fn(int a, int c){
    if(a>c)         
            if (c>a)
               {
                //    print('hello');
                   print(a);
               } 
            else
               {
                //    print('done'); 
                   a = a/4;
               }
    return a;
    }
    void main(){
        int c;
        fn(c,fn(c, fn(c, c)));
        int j = fn(c,c);
    }
}
