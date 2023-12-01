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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *current;
		current = head;
		while(current != NULL && current->next != NULL){
			if (current->val == current->next->val){
				current->next = current->next->next;
				continue;
			}
			current = current->next;
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
	head = new ListNode(1, head);
	head = new ListNode(1, head);
	head = new ListNode(1, head);
	head = new ListNode(1, head);
	head = new ListNode(3, head);
	head = new ListNode(5, head);
	head = new ListNode(6, head);
	print(head);
	Solution ob;
	ob.deleteDuplicates(head);
	cout<<"after"<<endl;
	print(head);
}