class Test{
void bar (int x, int y, int z){
    int i = x+y;
}

void foo ( int x, int y)
{
    //x = y;
    bar(x, y, x);
}

void Main(){
    int x, y, a;
    int[] b = new int[3];
    b[1] = 2;
    a= foo( x, y);
}
}

