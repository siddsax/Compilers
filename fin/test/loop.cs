//using System;

class test{
int dic(int a){
    int i = 0;
    while (a > 0){
        print(a);
        i++;
        a = a-5;
    }
    return i;
}
int Main(){	
	int i,k,res;
    res = 0;
    i = 0;
    int j =9;
    print(j);
	while(i < 10){
        j = 0;
		while(j < 10){
           k = dic(j);
			while(k < 10){
				res++;
               k++;
			}
           j++;
		}
        i++;
	}
    print(res);
}
}
