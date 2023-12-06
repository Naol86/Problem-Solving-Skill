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
    ListNode* removeElements(ListNode* head, int val) {
        if(head == NULL)
			return head;
		if (head->val == val)
			return removeElements(head->next, val);
		ListNode *current;
		current = head;
		while(current->next){
			if (current->next->val == val)
				current->next = current->next->next;
			else
				current = current->next;
		}
		return head;
    }
};