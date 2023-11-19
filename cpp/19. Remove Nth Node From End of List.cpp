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

	unsigned int len(ListNode* head){
		unsigned int a = 0;
		ListNode* current;
		current = head;
		while(current){
			a++;
			current = current->next;
		}
		return a;
	}

    ListNode* removeNthFromEnd(ListNode* head, int n) {
		unsigned int index, del;
		index = 0;
		del = len(head) - n;
		if (del == 0){
			if (head)
				return head->next;
			return NULL;
		}
		ListNode* current;
		current = head;
		while(index < del){
			if(index + 1 == del){
				current->next = current->next->next;
				return head;
			}
			current = current->next;
			index++;
		}
		return head;
    }
};

void print(ListNode* head){
	ListNode* current;
	current = head;
	while(current){
		if (current > current->next){
			cout<<"True"<<endl;
		}
		cout<<current->val<<current<<endl;
		current = current->next;
	}
}
