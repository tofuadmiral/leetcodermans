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
#include <vector>
#include <map>
#include <iostream>
using namespace std;


struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  };

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};



class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        // create a height balanced BST, i.e. depth never differs by two
        /*
            with an array, we'd start at middle and make root, then recursively 
            call the function on the array and keep adding children 
            so let's just put this linked list into an array (o(n)) linear time
            then do the same thing! to make the tree should take O(n) time as well
        
        */
        vector<int> nums = convertToVector(head);
        
        // now we have our array of numbers, so call our helper function to 
        // construct our tree from that
        TreeNode* root = arrayToBST(nums);
        return root;
    
    }
    
    TreeNode* arrayToBST(vector<int> nums){
        int numItems=nums.size();
        return TreeNode(nums[0])
    }
    
    
    vector<int> convertToVector(ListNode* head){
        // take in our head of linked list, then convert to an array
        vector<int> nums;
        ListNode* node=head;
        while((*node).next != NULL){
            nums.push_back((*node).val);
            node=(*node).next;
        }
        return nums;
    }
};