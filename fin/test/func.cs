class Test{
void pr(int var){
    print(var);
    return;
}
int bar (int x, int y, int z){
    int i = x*z + y;
    pr(i);
    return i ;
}

int foo ( int x, int y)
{
    //x = y;
    return bar(x, y, bar(y,y,y));
    // return;
}

void Main(){
    int x, y, a;
    int[] b = new int[3];
    b[1] = 2;
    x = 8;
    y = 9;
    a = foo( x, y);
    print(a);
}
}

