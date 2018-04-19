class Program {
    int Main() {
        int num;
        int i = 0;
        while (i<10) {
            num = num + 1;
            int j = 10;
            while (j > 1 ) {
                int k = 0;
                k = k + 1;
                j = j -1;
            }
            while(num < 100){
                num = num * 10;
                while( i > 2) {
                    i = i - 1;
                }
            }
            i = i + 1;
        }
        print(num);
        print(i);
    }
}
