/*

first some notes on pointers in c++

address operator = &, thus addr of myvar = &myvar

a pointer stores the address of a variable

thus, 
myvar=32
pointer = &myvar
print(*pointer) // gives us 32, the value pointed to by the addr of myvar, which is held in pointer
to dereference this, use the * operator
*/


#include <vector> 
#include <map>
using namespace std;


class Solution {
public:
    int missingNumber(vector<int>& nums) {
        // get a pointer to a vector of integers
        // thus, dereference this firsto access it
        
        // find the number that is missing
        
        /*
        solution: 
            add all the elements to a dictionary, with key as the number, and value 
            as 1 if we've seen it
            keep track of our maximum so far, and store that
            check from 0 to n and see if every variable is in the dictionary
            if a number isn't, then it's the missing number
            should be linear time to go through all the elements and add
            linear time to search thru all again
            linear space as well to store all of it
        
        */
        
        if(nums.size()==1){
            if (nums[0]==1) return 0;
            else return 1;
        }
        map<int, int> numbers;
        int max=0;
        for(int i=0; i< nums.size(); i++){
            if(nums[i]>max) max=nums[i];
            numbers[nums[i]]=1;
        }
        for(int i=0; i<max; i++){
            if(numbers.find(i)==numbers.end()){
                return i;
            }
        }
        return nums.size();
    }
};