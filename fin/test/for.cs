using System;

class Test{

// Does not care if the type of funtion is void or int - Need to be fixed
// Seg fault due to return (exit issue)
    void Main(){
        int i=8;
        // int b=0;
        // int c=1;
        // int d=99;
        while(i<=8 && i>=6){
            // print(d);
            if (i>=0){
                // System.print("yes\n");
                print(i);
                // print(c);
                // i++;
                i--;
            }
            else
            { 
                // System.print("no\n");
                print(i);
                // print(b);
                // i++;
                i--;
                // i++;
            }
    }
}
}

