class Hello 
{
//	void foo(int s)
//	{
//		print(foo(s));
//	}	
	int fact(int n)
	{
		int ans=1;
		int j = 2;
		int[] b = new int[5];
		b[3] = 3;
		while(j<=n){
			ans = ans*j;
			j++;
			//while(j<20){
				//int k;
				//b[4] = k < 20;
			//}
			
		}
	//	foo(ans);
		return ans;
	}

	void Main() 
	{	
		int[] a = new int[3];
		a[2] = 3;
		int f = fact(fact(a[2]));
		print(f);
	}
}
