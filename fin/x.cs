class A{

    int x;
    int func(){
        return x;
    }
    void func2(){
        x = 1;
        return;
    }
}

class C{

    int x;
    int func(){
        return x;
    }
    void func2(){
        x = 1;
        return;
    }
}

class B{
    int b;
    void Main(){
        int a;
        A x, y;
        C z;
        x = y+z;
        a = x.x + y.x;
        a = x.func();
    }

}
