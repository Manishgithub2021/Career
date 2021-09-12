package com.codewithmanish;

public class PerfectNo_PerfectNoBetweenRange {
	public boolean isPerfectNo(int num) {
		int sum=0;
		for(int i=1;i<num;i++) {
			if(num%i==0) {
				sum+=i;
			}
		}
		if(sum==num)
			return true;
		else
		return false;
	}
	public void perfectNoBetweenRange(int start, int stop) {
		int sum=0;
		for(int i=start;i<=stop;i++) {
			for(int j=1;j<i;j++) {
				if(i%j==0) {
					sum+=j;
				}
			}
			if(sum==i) {
				System.out.println(i+" is a perfect number");
			}
			sum=0;
		}
	}

}
