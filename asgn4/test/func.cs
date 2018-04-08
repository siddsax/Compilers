using System;



class Test{
void bar(){
    int i = 1;
}
void foo (int[] a, int x, int y)
{
    i = 3;
    x = y;
    bar();
}

void Main(){
    int x, y, a;
    int[] b;
    b[1] = 2;
    a= foo(b, x, y);
    return 0;
}
}

