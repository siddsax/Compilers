using System;

int main(){
	
	int i,j,k,res;
    res = 0;
    i = 0;
	while(i < 10){
        j = 0;
		while(j < 10){
            k = 0;
			while(k < 10){
				res += 1;
                k++;
			}
            j++;
		}
        i++;
	}

	System.print("res = %d\n", res);
}
