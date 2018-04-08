class Hello 
{
	int fact(int n)
	{
		int n;
		int ans=1;
		int j = 2;
		while(j<=n){
			ans = ans*j;
			j++;
		}
		return ans;
	}

	int Main() 
	{
		int f = fact(5);
		print(f);
		return 0;
	}
}