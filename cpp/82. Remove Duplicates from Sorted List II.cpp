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
        if (head == NULL || head->next == NULL)
			return head;
		if (head->val == head->next->val){
			ListNode* next;
			next = head;
			while(next!=NULL && head->val == next->val)
				next = next->next;
			return deleteDuplicates(next);
		}
		ListNode* current, * next, *slow;
		current = head;
		while (current!= NULL && current->next != NULL){
			if (current->val == current->next->val){
				next = current;
				while(next != NULL && next->val == current->val)
					next = next->next;
				slow->next = next;
				current = next;
				continue;
			}
			slow = current;
			current = current->next;
		}
		return head;
    }
};
