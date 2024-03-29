#include <iostream>

using namespace std;

struct Tree
{
    /* data */
    int data;
    Tree *left;
    Tree *right;
};



void inorder(Tree *root) {
    if (root == NULL) {
        return;
    }
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

void preorder(Tree *root) {
    if (root == NULL) {
        return;
    }
    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
}

void postorder(Tree *root) {
    if (root == NULL) {
        return;
    }
    postorder(root->left);
    postorder(root->right);
    cout << root->data << " ";
}


int main(){
    // Constructing a binary tree
    Tree* root = new Tree();
    root->data = 1;

    root->left = new Tree();
    root->left->data = 2;

    root->right = new Tree();
    root->right->data = 3;

    root->left->left = new Tree();
    root->left->left->data = 4;

    root->left->right = new Tree();
    root->left->right->data = 5;

    root->right->left = new Tree();
    root->right->left->data = 6;

    root->right->right = new Tree();
    root->right->right->data = 7;

    // Calling the inorder function
    inorder(root);

    
    return 0;
}