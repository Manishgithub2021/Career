
#include<conio.h>
#include<stdio.h>

struct node{
	int data;
	struct node *next;
};
struct node *head;

void insert(int num){
	struct node *last,*temp;
	if(!head){
		temp=(struct node *)malloc(sizeof(struct node *));
	temp->data=num;
	temp->next=NULL;
	head=temp;
		
	}
	else{
		temp=(struct node *)malloc(sizeof(struct node *));
	temp->data=num;
	temp->next=NULL;
	last=head;
	while(last->next!=NULL){
		last=last->next;
	}
	last->next=temp;
	}
	
	
	
};
void display(){
	struct node *last;
	if(!head){
		printf("\n\nNothing to display\n\n");
	}else{
		last=head;
		printf("\n\n********STARTED PRINTING DATA*******\n\n");
		while(last){
			printf("%d\n",last->data);
			last=last->next;
		}
		printf("\n\n***********FINISHED PRINTING DATA**********\n\n");
	}
	
};
void delete(){
	if(!head){
		printf("\n\n Queue is empty nothing to delete\n\n");
	}else if(head->next==NULL){
		struct node *temp;
		temp=head;
		printf("\n\nDeleted item is %d\n\n",head->data);
		head=NULL;
		free(temp);
		
	}else{
		struct node *first;
		first=head;
		printf("\n\nDeleted item is %d\n\n",head->data);
		head=head->next;
		free(first);
	}
}
void main(){
	printf("\nINSIDE MAIN LOOP\n\n");
	display();
	delete();
	insert(1);
	delete();
	delete();
	
	insert(2);
	insert(3);
	insert(4);
	insert(5);
	display();
	insert(6);
	insert(7);
	display();
	insert(8);
	insert(9);
	display();
	delete();
	display();
	delete();
     display();
};
