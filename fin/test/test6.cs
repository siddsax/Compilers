class Program {
    int d = 10;
    // int l,m,p;
    int fact(int y) {
        print(d);
        if (y <= 1) {
            return 1;
        }
        return y*fact(y-1) ;
    }
    // int doublefact(int x) {
    //     print(fact(x));
    //     print(d);
    //     return fact(x);
    // }
    int Main() {
        // int y;
        // y = 5;
        // // int x;
        // x = doublefact(y);
        // print(y);
        // print(x);
        print(fact(5));
    }
}
