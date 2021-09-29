package com.codewithmanish;

public class AckermannFunction {

	public static void main(String[] args) {
		System.out.println(Ackermann(1,2));
		// TODO Auto-generated method stub

	}
	public static int Ackermann(int m, int n) {
		if(m==0) {
			return n+1;
		}
		else if(m!=0 && n==0) {
			return Ackermann(m-1,1);
		}
		else if(m!=0 && n!=0) {
			return Ackermann(m-1,Ackermann(m,n-1));}
		else return 0;
	}

}
