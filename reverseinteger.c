//
//  reverseinteger.c
//  
//
//  Created by Ahmed Fuad Ali on 2018-09-24.
//

#include <stdio.h>


int reverse(int x) {
    
    // we need to reverse this integer
    // take the integer and mod by ten to get the ones place
    int remainder = 0;
    int reversed = 0;
    int tenpow = 0;
    
    if (x>0){
        while (x > 0){
            remainder = x % 10;
            x = x/10; // shave off the last digit
            // now add the digit to the new reversed number, but add backwards
            reversed = reversed * 10 + remainder;
        }
        
    }
    
    if (x<0){
        while (x < 0){
            remainder = x % 10;
            x = x/10; // shave off the last digit
            
            // now add the digit to the new reversed number, but add backwards
            reversed = reversed * 10 + remainder ;
        }
    }
    
    int newreversed = 0;
    while (reversed!=0){
        remainder = reversed%10;
        reversed /= 10;
        newreversed = newreversed*10 + remainder;
    }
    
    if (reversed == newreversed){
        return reversed;
    }
    else{
        return 0;
    }
    
}
