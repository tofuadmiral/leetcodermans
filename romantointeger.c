int romanToInt(char* s) {
    // convert a roman numeral to a regular integer
    
    int sum = 0;
    
    // loop for each item in the string

    for(int i = 0; i< sizeof(s); i++){
        
        // case I
        if (s[i] == 'I'){
            
            if (s[i + 1] == 'V'){
                sum--;
            }
            else if(s[i + 1] == 'X'){
                sum--;
            } 
            
            else{
                sum++;
            }
            
        }
        // case V
        if(s[i] == 'V'){
            sum+=5;
        }
        
        // case X
        if(s[i] == 'X'){
            if (s[i + 1] == 'L'){
                sum-=10;
            }
            else if(s[i + 1] == 'C'){
                sum-=10;
            } 
            else{
                sum+=10;
            }
            
        }
          // case L
        if(s[i] == 'L'){
            sum+=50;
        }
          // case C
        if(s[i] == 'C'){
            if (s[i + 1] == 'D'){
                sum-=100;
            }
            else if(s[i + 1] == 'M'){
                sum-=100;
            } 
            else{
                sum+=100;
            }
            
        }
          // case D
        if(s[i] == 'D'){
            sum+=500;
        }
          // case M
        if(s[i] == 'M'){
            sum+=1000;
        }
        if(s[i] == '\0'){
            break;
        }
    }
    return sum;
}