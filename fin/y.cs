class A{

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
        int b;
        A x;
        a = 1;
        b = a;
        if(a == b){
            int a;
            a = 2;
        }
        else{
            a = 3;
        }
    }

}
