package com.codewithmanish;

public class SelectionSort {

	public static void main(String[] args) {
		int[]arr= {12,3,4,1,2,3,4,5,6,7};
		for(int val:selectionsort(arr)) {
			System.out.println(val);
			
		}
		// TODO Auto-generated method stub

	}
	public static int[] selectionsort(int []arr) {
		int min,minpos=0,temp;
		for(int i=0;i<arr.length;i++) {
			min=arr[i];
			for(int j=i;j<arr.length;j++) {
				if(arr[j]<=min) {
					min=arr[j];
					minpos=j;
				}
			}
			temp=arr[i];
			arr[i]=min;
			arr[minpos]=temp;
			
			
		}
		return arr;
	}

}
