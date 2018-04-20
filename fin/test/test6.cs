class Program {
    int d = 10;
    int l,m,p;
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
        x = doublefact(y);
        print(x);
    }
}
