#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        // see whether i and j 
        // difference is t at most 
        // difference in positions is at most k
        for (int i=0; i<nums.size(); i++){
            for (int j=i; j<nums.size(); j++){
                if (abs(nums[i]-nums[j])>t and abs(i-j)>k ){
                    return false;
                }
            }
        }
        return true;
    }
};