package com.codewithmanish;

public class LinearSearch_BinarySearch {
	public void LinearSearch(int[]arr,int number) {
		int pos=0;
		
		for(int  i=0;i<arr.length;i++) {
			if(number==arr[i])
			{
				
				System.out.println(number+" is found at position "+i);
				return;
			}
		}
		System.out.println(number+" not found");
		
	}
	public void BinarySearch(int []arr, int number) {
		int start=0;
		int end=arr.length-1;
		while(start<=end) {
			int mid=(start+end)/2;
			if(arr[mid]==number) {
				System.out.println(number+" is found at position "+mid);
				return;
			}
			else if(number<arr[mid]) {
				end=mid-1;
			}
			else if(number>arr[mid]) {
				start=mid+1;
			}
		}
		System.out.println(number+" not found ");
		
	}

}
