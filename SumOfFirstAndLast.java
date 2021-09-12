package com.codewithmanish;

public class SumOfFirstAndLast {
	public static void main(String args[] ) {
		int value=sumFirstAndLastDigit(10);
		System.out.println("THE SUM IS "+value);
	
	   
	    // write your code here
	}
	 public static int sumFirstAndLastDigit(int number){
	        if(number<0){
	            return -1;
	        }
	        else{
	            if(number<=9){
	                 System.out.print(2*number);
	                return 2*number;
	               
	            }else{
	                int last=number%10;
	                System.out.println("LAST DIGIT IS"+last);
	                int temp=number;
	                System.out.print("TEMP BEFORE GOING TO LOOP IS "+temp);
	                while(temp>=10){
	                    temp=temp/10;
	                    System.out.println("TEMP INSIDE LOOP IS"+temp);
	                }
	                System.out.println("TEMP OUTSIDE LOOP IS"+temp);
	                System.out.println("SUM IS "+(temp+last));
	                return (temp+last);
	            }
	            
	        }
	        
	    }
}


