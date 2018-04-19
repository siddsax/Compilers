class foo{
    void main(){
        int c,d,e;
        c = 0;
        d = 1;
        e = 1;
        if (c && d)
            d++;
        else if (d & e) // bitwise and
            e++;
        else
            d--;
    }
}