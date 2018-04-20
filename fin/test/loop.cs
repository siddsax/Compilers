class test{
int Main(){
	
	int i,j,k,res;
    res = 0;
    i = 0;
	while(i < 10){
        j = 0;
		while(j < 10){
           k = 0;
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
