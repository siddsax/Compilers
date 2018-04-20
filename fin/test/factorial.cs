class Hello 
{
	// int n = 0;
	void foo(int s)
	{
		print(s);
		return;
	}	

	int fact(int n)
	{
		int ans=1;
		int j = 2;
		int[] b = new int[10];
		// int[] a = new int[10];
		b[3] = 3;
		while(j<=n){
			ans = ans*j;
			j++;
			// while(j<20){
			// 	int k;
			// 	b[4] = k < 20;
			// }
			
		}
	//	foo(ans);
		return ans;
	}

	void Main() 
	{	
		int[] a = new int[3];
		a[2] = 7;
		int f = fact(a[2]);
		foo(f);
		// return 0;
	}
}
