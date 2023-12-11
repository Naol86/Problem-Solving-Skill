#include <iostream>


using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    bool check(TreeNode* one, TreeNode* two){
		if(one == NULL && two == NULL)
			return true;
		if(one == NULL && two != NULL)
			return false;
		if(one != NULL && two == NULL)
			return false;
		if(one->val != two->val)
			return false;
		bool temp,temp2;
		temp = check(one->left,two->left);
		temp2 = check(one->right,two->right);
		return temp && temp2;
	}
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return check(p,q);
    }
};