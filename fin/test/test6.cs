class Program {
    int d;
    d = 2;
    int l,m,p;
    l = 6;
    m = d;
    int fact(int y) {
        if (y <= 1) {
            return 1;
        }
        return y*fact(y-1) ;
    }
    int doublefact(int x) {
        return d*fact(x);
    }
    int Main() {
        int y;
        y = 10;
        int x;
        x = fact(y);
        print(x);
    }
}