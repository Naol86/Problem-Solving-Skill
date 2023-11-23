#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
	void swap(ListNode **head, ListNode* current){
		ListNode* temp, *temp2;
		temp2 = *head;
		temp = *head;
		if ( temp->val > current->val){
			while(temp2->next != current)
				temp2 = temp2->next;
			temp2->next = current->next;
			current->next = temp;
			*head = current;
			return;
		}
		while(temp != current){
			if(temp->next->val > current->val){
				temp2 = temp;
				while(temp2->next != current)
					temp2 = temp2->next;
				temp2->next = current->next;
				current->next = temp->next;
				temp->next = current;
				break;
			}
			temp = temp->next;
		}
	}

    ListNode* insertionSortList(ListNode* head) {
        if(head == NULL || head->next == NULL)
			return head;
		ListNode* current, *temp;
		
		current =  head->next;
		while(current){
			temp = current->next;
			swap(&head, current);
			current = temp;
		}
		return head;
    }
};

void print(ListNode* head){
	ListNode* current;
	current = head;
	while (current){
		cout<<current->val<<endl;
		current = current->next;
	}
}

int main()
{
	ListNode* head;
	head  = new ListNode(4);
	head = new ListNode(2, head);
	head = new ListNode(7, head);
	head = new ListNode(8, head);
	head = new ListNode(1, head);
	head = new ListNode(3, head);
	head = new ListNode(5, head);
	head = new ListNode(6, head);
	// print(head);

	cout<<"after "<<endl;
	Solution ob;
	ob.insertionSortList(head);
	// print(head);
}