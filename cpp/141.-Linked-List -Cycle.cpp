#include <iostream>
using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL || head->next == NULL)
			return false;
		ListNode * current;
		current = head;
		while (current){
            if (current->next == NULL){
                return false;
            }
			if(current >= current->next){
                // cout<<current<<endl<<current->next<<endl;
				return true;}
			current = current->next;
		}
		return false;
    }
};