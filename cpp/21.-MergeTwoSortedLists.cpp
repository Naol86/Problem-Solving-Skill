#include<iostream>

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
		ListNode add(ListNode** head,int val){
			ListNode *new_node = new ListNode(val);
			ListNode* current;
			if (*head == NULL){
				*head = new_node;
				return (**head);
			}
			current = *head;
			while(current->next)
				current = current->next;
			current->next = new_node;
			return (**head);
		}
		ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
			ListNode *new_list = NULL;
			while(list1 || list2){
				if (list1 && list2){
					if (list1->val == list2->val){
						add(&new_list,list1->val);
						list1 = list1->next;
					}
					else if(list1->val < list2->val){
						add(&new_list,list1->val);
						list1 = list1->next;
					}
					else{
						add(&new_list,list2->val);
						list2 = list2->next;
					}
				}
				else if (list1){
					add(&new_list,list1->val);
					list1 = list1->next;
				}
				else{
					add(&new_list,list2->val);
					list2 = list2->next;
				}
			}
			return (new_list);
		}
};

