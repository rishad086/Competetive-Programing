#include<bits/stdc++.h>
using namespace std;
class node
{
public:
    int data;
    node* next;
};
void printlist(node* n)
{
    while(n!=NULL)
    {
        cout<<n->data<<" ";
        n=n->next;
    }
}
node* head=NULL;
node *temp=NULL;
 creation(int num)
{
    node *ptr;
    ptr=new node();
    ptr->data=num;
    ptr->next=NULL;
    if(head==NULL)
    {
        head=ptr;
        temp=ptr;
    }
    else
    {
        temp->next=ptr;
        temp=ptr;
    }
}
int main()
{
    int n,item,i;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>item;
        creation(item);
    }
    printlist(head);
}
