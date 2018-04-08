class Hello 
{
	void foo(int s)
	{
		print(foo(s));
	}	

	int fact(int n)
	{
		int ans=1;
		int j = 2;
		int[] b;
		b[3] = 3;
		while(j<=n){
			ans = ans*j;
			j++;
			while(j<20){
				int k;
				b[4] = k < 20;
			}
			
		}
		foo(ans);
		return ans;
	}

	int Main() 
	{	
		int[] a;
		a[2] = 4;
		int f = fact(a[2]);
		print(f);
		return 0;
	}
}