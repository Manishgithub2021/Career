package com.codewithmanish;

public class LargestPrime {
	public static void main(String args[]) {
		int prime=getLargetPrime(7);
		System.out.println("largest prime returned is"+prime);
	}
    public static int getLargetPrime(int number){
        if(number<2){
            return -1;
        }else{
        	System.out.println("number passed is "+number);
            int num[]=new int[10];
            int counter=-1;
           for(int i=2;i<=number;i++) {
        	   if(number%i==0) {
        		   num[++counter]=i;
        		   
        	   }
           }
           for(int i=0;i<=counter;i++) {
        	   System.out.println("All divider are"+num[i]);
           }
           int countflag=0;
           int num_of_prime=0;
           int primecounter=-1;
           int prime[]=new int[10];
           for(int i=0;i<=counter;i++) {
           	for(int j=2;j<=num[i];j++) {
           		if(num[i]%j==0) {
           			countflag++;
           			
           		}
           		
           	}
           	if(countflag==1) {
           		prime[++primecounter]=num[i];
           		
           	}
           	countflag=0;
           }
           for(int i=0;i<=primecounter;i++) {
        	   System.out.println("prime is"+prime[i]);
           }
           if(primecounter<0) {
        	   return -1;
           }
           else {
        	   return prime[primecounter];
           }
        }
        
        
    }
    // write your code here
}
