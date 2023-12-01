#include <iostream>
#include <stack>

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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
		if (head == NULL || head->next == NULL || left == right)
			return head;
        if (left == 1){
			ListNode* zero = new ListNode(1,head);
			zero = reverseBetween(zero,left+1,right+1);
			return zero->next;
		}
        stack<ListNode*> my_lis;
		ListNode* current,*point,*temp;
		int i = 0;
		temp = head;
		while(temp && i < right){
			if (i+1>= left){
				my_lis.push(temp);
			}
			temp = temp->next;
			i++;
		}
		i = 1;
		current = head;
		while(current && i+1 < left)
		{
			current = current->next;
			i++;
		}
		while(!my_lis.empty()){
			current->next = my_lis.top();
			my_lis.pop();
			current = current->next;
		}
		current->next = temp;
		return head;
    }
};
