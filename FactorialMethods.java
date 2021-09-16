package com.codewithmanish;

public class FactorialMethods {
public int factorial(int num) {
	if(num==0)
		return 1;
		else
			return num*factorial(num-1);
}
public void factorialOfFirstNNaturalNumbers(int firstN) {
	for(int i=1;i<=firstN;i++) {
		System.out.println(new FactorialMethods().factorial(i));
	}
}
public void factorialOfNumberBetweenGivenRange(int start, int end) {
	for(int i=start;i<=end;i++) {
		System.out.println(new FactorialMethods().factorial(i));
	}
}
}
