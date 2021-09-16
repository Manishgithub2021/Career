package com.codewithmanish;

public class FibbonaciMethods {
	public int  fibbonaci(int num) {
		if(num==0)
			return 0;
		else if(num==1)
			return 1;
		else
			return fibbonaci(num-1)+fibbonaci(num-2);
	}

}
