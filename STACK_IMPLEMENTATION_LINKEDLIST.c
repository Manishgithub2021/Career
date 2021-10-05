//STACK IMPLEMENTATION USING SINGLE LINKED LIST
#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
// Defining struct
struct node{
	int data;
	struct node *next;
};
struct node *head;
void display(){
	if(!head){
		printf("\nStack is empty\n");
	}
	else{
		struct node *temphead;
		temphead=head;
		printf("\n***STARTED PRINTING DATA*********\n\n");
			while(temphead){
				
		printf("%d\n",temphead->data);
		temphead=temphead->next;
	}
	printf("\n******ALL DATA PRINTED******\n\n");
	}

	
};
void insert(int data){
	struct node *temp,*temphead;
	temp=(struct node *)malloc(sizeof(struct node *));
	temp->data=data;
	temp->next=NULL;
	if(!head){
		head=temp;
	}
	else{
			temphead=head;
	while(temphead->next!=NULL){
		temphead=temphead->next;
	}
	temphead->next=temp;
	}

};
void pop(){
	struct node *last,*secondlast;
	last=head;
	secondlast=head;
	if(!last){
		printf("\nStack is empty, nothing to delete\n");
	}
	else if(last->next==NULL){
		printf("\ndeleted data is:%d\n\n",last->data);
		free(last);
		head=NULL;
	}
	
	
	
	else{
		while(last->next!=NULL){
			last=last->next;
		}
		
		while(secondlast->next!=last){
			secondlast=secondlast->next;
		}
		
		secondlast->next=NULL;
		printf("\ndeleted data is:%d",last->data);
		free(last);
	}
	
};
void main(){
while(1){
	printf("\n**************CHOOSE A OPTION**********************\n");
	printf("\n****** 0  : Exit***************");
	printf("\n****** 1  : Insert*************");
	printf("\n****** 2  : Delete*************");
	printf("\n****** 3  : Display************");
	printf("\n Type your choice:  ");
    int choice;
	scanf("%d",&choice);
	
	switch(choice){
		case 0:printf("\nExiting");
		return;
		case 1: printf("\nWhat to insert? ");
		int num;
		scanf("%d",&num);
		insert(num);
		printf("\nInserted successfully");
		break;
		case 2:pop();
		break;
		case 3:display();
		break;
		default:printf("\nWrong choice");
		return;
	}
	
	
}
	
	
	
	
};
