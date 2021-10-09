#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

//SINGLE LINKED LIST IMPLEMENTATION 

struct node{
	int data;
	struct node *next;
};
struct node *head;
void insertatBegining(int num){
	struct node *temp;
	temp=(struct node *)malloc(sizeof(struct node *));
	temp->data=num;
	if(!head){
		
		temp->next=head;
		
		head=temp;
		
		
	}else{
		temp->next=head;
		head=temp;
	}
	
	
	
};
void insertatEnd(int num){
	struct node *temp,*last;
	temp=(struct node *)malloc(sizeof(struct node *));
	temp->data=num;
	if(!head){
		
		temp->next=head;
		
		head=temp;
		
		
	}else{
		last=head;
		while(last->next!=NULL){
			last=last->next;
		}
		last->next=temp;
		temp->next=NULL;
	}
};

void DeleteAtBegining(){
	struct node *first;
	if(!head){
		printf("\n\n****nothing to delete**********\n\n");
	}else{
		first=head;
		printf("\n\nDeleted number is %d\n\n",head->data);
		head=head->next;
		free(first);
	}
	
};
void DeleteAtEnd(){
	struct node *first,*last,*secondlast;
	if(!head){
		printf("\n\n****nothing to delete**********\n\n");
	}
	else if(head->next==NULL){
		first=head;
		printf("\n\nDeleted item is %d\n\n",head->data);
		head=NULL;
		free(first);
		
	}else{
		last=head;
		secondlast=head;
		
		while(last->next!=NULL){
			last=last->next;
		}
		while(secondlast->next!=last)
		secondlast=secondlast->next;
		
		secondlast->next=NULL;
		free(last);
		
	}
};


void findNumber(int num){
	struct node *temp;
	int counter=-1;
	temp=head;
	while(temp){
		counter++;
		if(temp->data==num){
			printf("\n\nNumber %d is found at index %d\n\n",num,counter);
			return;
		}
		temp=temp->next;
	}
	printf("\n\nNumber is not found\n\n");
	
};



void display(){
	struct node *temp;
	if(!head){
		printf("\n\n******NOTHING TO DISPLAY***********\n\n");
	}
	else{
		printf("\n\n***********PRINTING STARTED*****************\n\n");
		temp=head;
		int counter=0;
		while(temp){
			counter++;
			printf("\n %d\n\n",temp->data);
			temp=temp->next;
			
		}
		printf("\n\n**************PRINTING FINISHED****************\n\n");
	}
	
};
void main(){
	printf("\n\n**********WELCOME TO WORLD OF SINGLE LINKED LIST**************\n\n");
	//DeleteAtBegining();
	insertatBegining(5);
	insertatBegining(6);
	insertatBegining(7);
	//DeleteAtBegining();
	display();
	//DeleteAtBegining();
		//display();
	DeleteAtEnd();
	display();
	DeleteAtEnd();
	display();
	DeleteAtEnd();
	display();
	DeleteAtEnd();
	display();
	
 
};
