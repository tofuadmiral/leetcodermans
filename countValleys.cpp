#include <bits/stdc++.h>

using namespace std;

// Complete the countingValleys function below.
int countingValleys(int n, string s) {
    
    // keep track of how far above sea level we are
    int pos = 0;
    
    // keep track of valleys
    int numvalleys = 0;
    
    
    
    // iterate thru the string
    for(int i =0; i<n; i++){ 
        
        // now figure out whether in valley or not 
        if(pos==0 && s[i]=='D'){
            // at sea, going down, starting valley 
            numvalleys++;
        }

        if(pos==-1 && s[i]=='U'){
            // below sea, going up, so ending valley
            numvalleys++;
        }
        
        // calculate our relative position
        if(s[i] == 'U'){
            pos++;
        }
        else if(s[i] =='D'){
            pos--;
        }

    }
    
    // numvalleys should be 2* how many valleys we're at, so then divide by two
    numvalleys /= 2;
    return numvalleys;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}