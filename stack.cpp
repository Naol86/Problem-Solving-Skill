#include <iostream>

using namespace std;

struct stack
{
    /* data */
    int data;
    stack *next;
};

stack *top = NULL;

void push(int data)
{
    stack *temp = new stack();
    temp->data = data;
    temp->next = top;
    top = temp;
}

void pop()
{
    if (top == NULL)
    {
        cout << "Stack is empty" << endl;
        return;
    }
    stack *temp = top;
    top = top->next;
    delete temp;
}

int peek()
{
    if (top == NULL)
    {
        cout << "Stack is empty" << endl;
        return -1;
    }
    return top->data;
}

int main() {
    push(1);
    push(2);
    push(3);
    cout << peek() << endl;
    pop();
    cout << peek() << endl;
    pop();
    cout << peek() << endl;
    pop();
    cout << peek() << endl;
    pop();
    // return 0;
}