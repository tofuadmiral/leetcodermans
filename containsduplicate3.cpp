#include <cstdlib>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        
        // want to see if there are two distinct i and j
        // thus, if more than one doesn't count
        // and if none, return false as well
        
        // intitial checks: empty list or one element list
        if (nums.size()==1 or 0) return false;
        
        int found =0; // initially we've found zero possible candidates
        
        // now loop through and see if a candidate is found, and add to the number 
        // we've already seen
        for(int i=0; i<nums.size(); i++){
            // loop through every number, check other index
            for(int j=i; j++; j<nums.size() or j<(i+k)){
                
                // check absolute diff bw elements and indices, if 
                // satisifies requirements, add to found 
                if(abs(long(nums[i])-long(nums[j]))<(t+1) and abs(i-j)<(k+1)){
                    found++;
                }
            }
        }
        
        // check how many we've found
        if (found==1){
            return true;
        }
        else return false;
        
    }
};