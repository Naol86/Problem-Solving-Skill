#include <iostream>

using namespace std;

struct Tree
{
    /* data */
    int data;
    Tree *left;
    Tree *right;
};

void insert_in_BST(Tree *&root, int data)
{
    if (root == NULL)
    {
        root = new Tree();
        root->data = data;
        root->left = root->right = NULL;
        return;
    }
    if (data < root->data)
    {
        insert_in_BST(root->left, data);
    }
    else
    {
        insert_in_BST(root->right, data);
    }
}

void search(Tree *root, int data)
{
    if (root == NULL)
    {
        cout << "Element not found" << endl;
        return;
    }
    if (root->data == data)
    {
        cout << "Element found" << endl;
        return;
    }
    if (data < root->data)
    {
        search(root->left, data);
    }
    else
    {
        search(root->right, data);
    }
}

void delete_node(Tree *&root, int data)
{
    if (root == NULL)
    {
        cout << "Element not found" << endl;
        return;
    }
    if (data < root->data)
    {
        delete_node(root->left, data);
    }
    else if (data > root->data)
    {
        delete_node(root->right, data);
    }
    else
    {
        if (root->left == NULL)
        {
            Tree *temp = root->right;
            delete root;
            root = temp;
        }
        else if (root->right == NULL)
        {
            Tree *temp = root->left;
            delete root;
            root = temp;
        }
        else
        {
            Tree *temp = root->right;
            while (temp->left != NULL)
            {
                temp = temp->left;
            }
            root->data = temp->data;
            delete_node(root->right, temp->data);
        }
    }
}