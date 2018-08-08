class Program {
    // int max = 10;
    int mul(int x, int y) {
        int z;
        if (x > y) {
            return x-y;
        } 
        else {
            return y-x;
        }
        // print(max);
    }
    void Main() {
        int max;
        int num =1;
        int[] numbers = new int[10];
        int i = 1;
        while (i< 6)
        {
            numbers[i] = i;
            i++;
        }
        int y = mul(2,mul(3,6));
        max = 5;
        numbers[2] = 3 + numbers[1];
        while ( max > num && num < 3) {
            num = num + 1;
        }
        print(num);
        print(y);
        print(numbers[2]);
        print(numbers[1]);
        print(numbers[5]);
        max = num = 1;
//	return;
    }
}
