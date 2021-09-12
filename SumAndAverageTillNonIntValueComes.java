package com.codewithmanish;
import java.util.Scanner;

public class SumAndAverageTillNonIntValueComes {

	public static void main(String[] args) {
		inputThenPrintSumAndAverage();

	}
	
	 
	//public class InputCalculator {
	    public static void inputThenPrintSumAndAverage(){
	        int sum=0;
	        long avg=0;
	        int counter=0;
	        Scanner sc=new Scanner(System.in);
	        if(!sc.hasNextInt()) {
	        	System.out.print("SUM = "+sum+" AVG = "+avg);
	        }
	        else {
	        while(sc.hasNextInt()){
	        	int num=sc.nextInt();
	        	sum=sum+num;
	        	counter=counter+1;
	        	
	            
	          
	        }
	        avg=Math.round(((double)sum/(double)counter));
	        System.out.print("SUM = "+sum+" AVG = "+avg);
	        
	    }
	    }
}
	    // Write your code here
	//}
//}
