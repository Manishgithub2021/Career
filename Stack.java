package com.codewithmanish;

import java.util.*;

public class Stack {
	public static int top=-1;
	public static int[] arr=new int[10];
	
	public static void main(String args[]) {
	
		int num;
		
		
		
	
		while(true) {
			System.out.println("0 :Exit");
			System.out.println("1 : Display");
			System.out.println("2 : Insert");
			System.out.println("3 : Delete");
			System.out.println("4 : Top element");
			System.out.println("5 : isEmpty");
			System.out.println("6 : isFull\n");
			Scanner sc=new Scanner(System.in);
			System.out.println("Enter your choice\n");
			num=sc.nextInt();
			sc.nextLine();
			switch(num) {
			case 1:
				display();
				break;
			case 2:
				insert();
				break;
			case 3:
				delete();
				break;
			case 4:top();
			break;
			
			case 5: 
				System.out.println("isEmpty: "+isEmpty());
			break;
			case 6:
				System.out.println("isFull :"+isFull());
				break;
			case 0:
				System.out.println("Exiting now");
				return;
				default:
					return;
			}
			
		}
		
		
		
	}
	static boolean isEmpty() {
		if(top==-1) {
			return true;
		}
		else
			return false;
	}
	static boolean isFull() {
		if(top==9) {
			return true;
		}
		else
			return false;
	}
	static void display() {
		if(isEmpty()) {
			System.out.println("Nothing to display ,stack is empty\n");
		}
		else {
			for(int i=0;i<=top;i++) {
				System.out.println("at "+i+" position elemnt is "+arr[i]);
			}
		}
	}
	static void delete() {
		if(isEmpty()) {
			System.out.println("Nothing to delete ,stack is empty");
		}
		else {
			System.out.println("Deleted item is "+arr[top]);
			top=top-1;
		}
		}
	static void top() {
		if(isEmpty()) {
			System.out.println("Stack is emtpy ,nothing at top");
			
		}else {
			System.out.println( arr[top])
			;
		}
		
	}
	static void insert() {
		if(isFull()) {
			System.out.println("Stack is full ,can't insert");
		}else {
		System.out.println("Enter element to insert");
		Scanner sc=new Scanner(System.in);
		int num=sc.nextInt();
		arr[++top]=num;
		System.out.println("\n After inserting elements in array is:\n");
		display();}
		
	}
		
	}
	


