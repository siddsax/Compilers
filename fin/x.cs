class A{

    int x;
    int func(){
        return x;
    }
    void func2(){
        x = 1;
    }
}

class C{

    int x;
    int func(){
        return x;
    }
    void func2(){
        x = 1;
    }
}

class B{
    int b;
    void Main(){
        int a;
        A x, y;
        C z;
        x = y+z;
        a = x.func();
        x.func2();
        y.func2();
        z.func2();
    }

}
