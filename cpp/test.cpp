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
        ListNode* current, *temp;
		if (head == NULL || head->next == NULL)
			return head;
		if(head->val == head->next->val){
			int tem = head->val;
			while(head && head->val != tem){
				head = head->next;
			}
			return deleteDuplicates(head);
		}
		if(head->next->next == NULL)
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

int main()
{
	ListNode* head = new ListNode(0);
	head = new ListNode(1,head);
	head = new ListNode(2,head);
	print(head);
}