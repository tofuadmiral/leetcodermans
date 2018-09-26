int romanToInt(char* s) {
    // convert a roman numeral to a regular integer
    
    int ones = 0;
    int fives= 0; 
    int tens = 0;
    int fifties= 0;
    int hundos= 0;
    int fhundos= 0;
    int thousands = 0;
    
    // loop for each item in the string

    for(int i = 0; i< sizeof(s); i++){
        
        // case I
        if (s[i] == 'I'){
            
            if (s[i + 1] == 'X'){
                ones--;
            }
            else if(s[i + 1] == 'V'){
                ones--;
            } 
            else{
                ones++;
            }
            
        }
        // case V
        if(s[i] == 'V'){
            fives++;
        }
        
        // case X
        if(s[i] == 'X'){
            if (s[i + 1] == 'L'){
                tens--;
            }
            else if(s[i + 1] == 'C'){
                tens--;
            } 
            else{
                tens++;
            }
            
        }
          // case L
        if(s[i] == 'L'){
            fifties++;
        }
          // case C
        if(s[i] == 'C'){
            if (s[i + 1] == 'D'){
                hundos--;
            }
            else if(s[i + 1] == 'M'){
                hundos--;
            } 
            else{
                hundos++;
            }
            
        }
          // case D
        if(s[i] == 'D'){
            fhundos++;
        }
          // case M
        if(s[i] == 'M'){
            thousands++;
        }
    }
    return (ones + fives*5 + tens*10 + fifties*50 + hundos*100 + fhundos*500 + thousands*1000);

}