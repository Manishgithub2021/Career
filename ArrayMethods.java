package com.codewithmanish;

import java.util.Arrays;

public class ArrayMethods {
	public  int MaxValueInArray(int[]arr) {
		int max=arr[0];
		for(int i=1;i<arr.length;i++) {
			if(arr[i]>max) {
				max=arr[i];
			}
		}
		return max;
		
	}
	public  int MinValueInArray(int[]arr) {
		int min=arr[0];
		for(int i=1;i<arr.length;i++) {
			if(arr[i]<min) {
				min=arr[i];
			}
		}
		return min;
		
	}
	public  int[] SortArrayInAscendingOrder(int[]arr) {
		//System.out.println("ORIGINAL ARRAY IS"+Arrays.toString(arr));
		int min,temp;
		for(int j=0;j<arr.length;j++) {
		for(int i=0;i<arr.length-1-j;i++) {
			if(arr[i]>arr[i+1]) {
				temp=arr[i];
				arr[i]=arr[i+1];
				arr[i+1]=temp;
			}
			
			
		}
		//System.out.println("Array after"+j+"th iteration is"+Arrays.toString(arr));
		}
		return arr;
		
	}
	public  int[] SortArrayInDescendingOrder(int[]arr) {
		//System.out.println("ORIGINAL ARRAY IS"+Arrays.toString(arr));
		int min,temp;
		for(int j=0;j<arr.length;j++) {
		for(int i=0;i<arr.length-1;i++) {
			if(arr[i]<arr[i+1]) {
				temp=arr[i];
				arr[i]=arr[i+1];
				arr[i+1]=temp;
			}
			
			
		}
		//System.out.println("Array after"+j+"th iteration is"+Arrays.toString(arr));
		}
		return arr;
		
	}
	
	public int[] reverseArray(int []arr) {
		int length=arr.length;
		int mid;
		if (length%2==0)
				mid=length/2;
		else
			mid=(length+1)/2;
		for(int i=0;i<mid;i++) {
			int temp=arr[i];
			arr[i]=arr[length-1-i];
			arr[length-1-i]=temp;
		}
		
		return arr;
	}
	public int sumOfArray(int []arr) {
		int sum=0;
		for(int i=0;i<arr.length;i++) {	
			sum+=arr[i];
		}
		return sum;
	}
	public double averageOfArrayElements(int []arr) {
		double sum=0;
		for(int i=0;i<arr.length;i++) {
			sum+=arr[i];
		}
		return sum/arr.length;
	}
	public int[] allPrimesInArray(int []arr) {
		int []primearray=new int[arr.length];
		int counter=-1;
		int flag=0;
		for(int i=0;i<arr.length;i++) {
			for(int j=1;j<=arr[i];j++) {
				if(arr[i]%j==0) {
					flag++;
					
				}
			}
			if(flag==2) {
				primearray[++counter]=arr[i];
			}
			flag=0;
		}
		//System.out.println(counter);
		int primearraynew[]=new int[counter+1];
	    for(int i=0;i<=counter;i++) {
	    	primearraynew[i]=primearray[i];
	    }
	    primearray=null;
		return primearraynew;
	}
	public int secondMaxElementInArray(int []arr) {
		
		if(arr.length==0) {
			return -1;
		}
		else if(arr.length==1) {
			return 0;
		}
		else if(arr.length==2) {
			int max=arr[0];
			if(arr[1]>max) {
				return max;
			}
			else {
				return arr[1];
			}
		}
		else {
			//int[]arr1=new int[2];
			
			int max=arr[0];
			int maxpos=0;
			for(int i=0;i<arr.length;i++) {
				if(arr[i]>max)
				{
					//max=arr[i];
					maxpos=i;
				}
			}
			//arr1[0]=max;
			arr[maxpos]=Integer.MIN_VALUE;
			max=arr[0];
			//maxpos=0;
			for(int i=0;i<arr.length;i++) {
				if(arr[i]>max)
				{
					max=arr[i];
					
				}
			}
			return max;
			
			
	}
	}
}




