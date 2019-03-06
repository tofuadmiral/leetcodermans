/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        // elements are in a single list, sorted in ascending
        // convert to height balanced binary search tree
        // this means middle value at top, then go greater and less than 
        // accordingly
        
        /*
            algorithm:
            - split into half and take middle value
                - edge: if only 2, or only one
            - call recursively on the right half and left half 
            - each call, add to the list 
            - function takes in current list, 
        
        */
        
    }
    
    vector<int> convertToArray(ListNode* head){
        // convert the singly linked list into a sorted array
        vector<int> numbers;
        while((*head).next()!=NULL){
            numbers.push_back((*head).val);
        }
        
    }
    
};