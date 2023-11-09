#include <bits/stdc++.h>
using namespace std;

struct node{
    int data;
    struct node* left;
    struct node* right;
};

struct node* newnode(int data){
    struct node* node = (struct node*)malloc(sizeof(struct node));
    node->data = data;
    node->left = NULL;
    node->right = NULL;

    return (node);
}

bool check(struct node* root, int low, int high){
    if(root == NULL){
        return true;
    }
    int v = root->data;
    if((v>low && v<high) && check(root->left, low, v) && check(root->right, v, high)){
        return true;
    }
    return false;
}

bool isBST(struct node* n){
    if (check(n, INT_MIN, INT_MAX)){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    struct node* root = newnode(4);
    root->left = newnode(2);
    root->right = newnode(5);
    root->left->left = newnode(1);
    root->left->right = newnode(3);
    cout<<(isBST(root))<<endl;
    return 0;
}
