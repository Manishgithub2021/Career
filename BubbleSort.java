package com.codewithmanish;

public class BubbleSort {

	public static void main(String[] args) {
		int[] arr= {0,5,2,10,40,32,34,1};
		int [] arr1= {10,8,4,20};
		int [] arr2= {1};
		int [] arr3= {};
	    int [] res=bubblesort(arr);
	    for(int val:res)
	    	System.out.println(val);
		
		// TODO Auto-generated method stub

	}
	public static int[] bubblesort(int[] arr) {
		int temp;
		for(int i=0;i<arr.length;i++) {
			for(int j=0;j<arr.length-i-1;j++) {
				if(arr[j]>arr[j+1]) {
					temp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=temp;
				}
				
			}
		}
		return arr;
		
	}

}
