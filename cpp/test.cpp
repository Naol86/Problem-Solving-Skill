#include <iostream>

using namespace std;

struct Node
{
	int val;
	Node* next;
	Node() : val(0), next(NULL) {}
	Node(int x) : val(x), next(NULL) {}
	Node(int x, Node* next) : val(x), next(next) {}
};

void print(Node* head)
{
	while(head){
		cout<<head->val<<endl;
		head = head->next;
	}
}


int main()
{
	Node *temp= new Node(23);
	temp = new Node(43,temp);
	// temp->val = 12;
	// temp->next = NULL;
	print(temp);
}
