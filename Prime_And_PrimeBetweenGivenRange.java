package com.codewithmanish;

public class Prime_And_PrimeBetweenGivenRange {
	public boolean isPrime(int number) {
		int counter=0;
		for(int i=1;i<=number;i++) {
			if(number%i==0) {
				counter++;
			}
		}
		if(counter==2)
			return true;
		else
			return false;
		
	}
	public void primeBetweenGivenRangeIncludingStartAndEnd(int start,int end) {
		int counter=0;
		Prime_And_PrimeBetweenGivenRange prime=new Prime_And_PrimeBetweenGivenRange();
		for(int i=start;i<=end;i++) {
			boolean isprime=prime.isPrime(i);
			if(isprime) {
				System.out.println(i+"  is prime ");
				counter++;
			}
		}
		if(counter==0) {
			System.out.println("No prime number found between given range "+start+" and "+end);
		}
		else
			System.out.println("Total "+counter+" prime number found between given range");
	}

}
