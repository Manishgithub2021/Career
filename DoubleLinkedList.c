#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct node{
	struct node *prev;
	int data;
	struct node *next;
};
struct node *head;
void display(){
	struct node *temp;
	temp=(struct node *)malloc(sizeof(struct node *));
	if(!head){
		printf("\n\n**********EMPTY***********\n\n");
	}
	else{
		temp=head;
		printf("\n\n**********START PRINTING DATA************\n\n\n");
		while(temp){
			printf("\n\n%d\n\n",temp->data);
			temp=temp->next;
			
		}
		printf("\n\n********ALL DATA PRINTED*****************\n\n\n");
	}
};
void insertAtBegining(int num){
	struct node *temp;
	temp=(struct node *)malloc(sizeof(struct node *));
	
		if(!head){
			temp->data=num;
		temp->next=NULL;
		temp->prev=NULL;
		head=temp;
		
	}else{
		
		
		temp->data=num;
		temp->prev=NULL;
		temp->next=head;
		
		head=temp;
		
	}
	
};
void insertAtEnd(int num){
	struct node *temp,*last;
	temp=(struct node *)malloc(sizeof(struct node *));
	
		if(!head){
			temp->data=num;
		temp->next=NULL;
		temp->prev=NULL;
		head=temp;
		
	}else{
		temp->data=num;
		temp->next=NULL;
		last=head;
		while(last->next!=NULL){
			last=last->next;
		}
		last->next=temp;
		temp->prev=last;
		
	}
	
};
void deleteAtBegining(){
		if(!head){
	printf("\n\n*******NOTHING TO DELETE**************\n\n");
		
	}else{
		printf("\n\ndeleted num is:%d \n\n",head->data);
		struct node *first;
		first=head;
		head=head->next;
		
		free(first);
	}
};
void deleteAtEnd(){
	if(!head){
	printf("\n\n*******NOTHING TO DELETE**************\n\n");
		
	}
	else if(head->next==NULL){
		struct node *temp;
		temp=head;
		printf("\n\ndeleted number is %d",temp->data);
		head=head->next;
		free(temp);
	}
	else{
		struct node *last,*secondlast;
		last=head;
	    secondlast=head;
		while(last->next!=NULL){
			secondlast=last;
			last=last->next;
			
		}
	
		printf("\n\n delted number is %d",last->data);
		secondlast->next=NULL;
		free(last);
		
		
	}
};
void main(){
	printf("\n*********WELCOME TO DOUBLE LINKED LIST WORLD**************\n");
	printf("\n\nINSERTING AT BEGINING\n\n");
	insertAtBegining(5);
	insertAtBegining(4);
	insertAtBegining(3);
	insertAtBegining(2);
	insertAtBegining(1);
	display();
	printf("\n\nINSERTING AT END\n\n");
	insertAtEnd(6);
	insertAtEnd(7);
	insertAtEnd(8);
	display();
	printf("\n\n********DELETING AT BEGINING\n\n");
	deleteAtBegining();
	deleteAtBegining();
	deleteAtBegining();
	deleteAtBegining();
	deleteAtBegining();
	deleteAtBegining();
	deleteAtBegining();
	deleteAtBegining();
	deleteAtBegining();
	deleteAtBegining();
	printf("\n\nINSERTING AT BEGINING\n\n");
	insertAtBegining(5);
	insertAtBegining(4);
	insertAtBegining(3);
	insertAtBegining(2);
	insertAtBegining(1);
	display();
	printf("\n\nINSERTING AT END\n\n");
	insertAtEnd(6);
	insertAtEnd(7);
	insertAtEnd(8);
	display();
	printf("\n\n********DELETING AT END\n\n");
	deleteAtEnd();
	deleteAtEnd();
	deleteAtEnd();
	deleteAtEnd();
	deleteAtEnd();
	deleteAtEnd();
	deleteAtEnd();
	deleteAtEnd();
		deleteAtEnd();
			deleteAtEnd();
	
	
	

}
