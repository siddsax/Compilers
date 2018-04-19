class test 
{
	int Main() 
	{
		int i = 0;
		// char j="charvar";
		int[] a = new int[10];
		a[i] = 3;
		if (i < 4)
			a[i]++;
		if (i > 1)
			a[i]--;
		else 
			a[i] = 1;
		print(a[0]);
	}
}
