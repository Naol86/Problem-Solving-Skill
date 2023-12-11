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
    int find(TreeNode* head, int n){
		if(head == NULL)
			return n;
		int _max;
		_max = find(head->left,n+1) > find(head->left,n+1) ? find(head->left,n+1) : find(head->left,n+1);
		return _max;
	}
	int maxDepth(TreeNode* root) {
        int ans;
		ans = find(root,0);
		return ans;
    }
};