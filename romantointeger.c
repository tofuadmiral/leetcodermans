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
            ones++;       
        }
        // case V
        if(s[i] == 'V'){
            fives++;
        }
        // case X
        if(s[i] == 'X'){
            tens++;
        }
          // case L
        if(s[i] == 'L'){
            fifties++;
        }
          // case C
        if(s[i] == 'C'){
            hundos++;
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
    return (ones + fives*5 + tens*10 + fifties*50 + hundos*100 + fhundos*500 + thousands*1000 );
}