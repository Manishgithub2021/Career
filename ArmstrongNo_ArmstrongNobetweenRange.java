package com.codewithmanish;

public class ArmstrongNo_ArmstrongNobetweenRange {
	public boolean isArmStrong(int num) {
		int sum=0;
		int rem,temp,number;
		number=num;
		while(number>0) {
			rem=number%10;
			sum+=(rem*rem*rem);
			number=number/10;
		}
		if(sum==num)
			return true;
		else
		return false;
	}
	public void armStrongBetweenRange(int start, int stop) {
		ArmstrongNo_ArmstrongNobetweenRange armstrong=new ArmstrongNo_ArmstrongNobetweenRange();
		for(int i=start;i<=stop;i++) {
			if(armstrong.isArmStrong(i)) {
				System.out.println(i+"is armstrong");
			}
		}
	}

}
