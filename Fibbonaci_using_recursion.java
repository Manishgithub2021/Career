package com.codewithmanish;

import java.util.Scanner;

public class Fibbonaci_using_recursion {
	public static void main(String args[]) {
		int how_many_num;
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter how many fibbonaci no to be generated: ");
		how_many_num=sc.nextInt();
		for(int i=0;i<how_many_num;i++) {
			System.out.println(fibbo(i));
		}
		
		
	}
	public static int fibbo(int num) {
		if(num<=0)
			return 0;
		else if (num==1)
			return 1;
		else
			return fibbo(num-1)+fibbo(num-2);
	}

}
