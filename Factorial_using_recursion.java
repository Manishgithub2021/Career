package com.codewithmanish;

import java.util.Scanner;

public class Factorial_using_recursion {
	public static void main(String args[]) {
		Scanner sc=new Scanner(System.in);
		int num;
		System.out.println("Enter the number: ");
		num=sc.nextInt();
		System.out.println("Factorial of "+num+" is "+fact(num));
		
	}
	public static int fact(int num) {
		if(num==0)
			return 1;
		else
			return num*fact(num-1);
	}

}
