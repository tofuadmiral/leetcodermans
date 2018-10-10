#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the sockMerchant function below.
int sockMerchant(int n, vector<int> ar) {
    
    // ar is a vector, dynamically resizing array. n is the number of elements we have
    // ar is the socks data
    
    // let's make a map, key is the sock color, value is the number of those socks
    std::map<int, int> sockLookup;
    
    // add everything to the map 
    for (int i =0; i<n;i++){
        
        // if color isn't already in the map, add it to the map 
        if(sockLookup.find(ar[i]) == sockLookup.end()){
            // key isn't in the map, so insert it
            sockLookup.insert(std::pair<int, int>(ar[i], 1));
        }
        else { // this means key IS in the map, so we just have to increment it 
            sockLookup[ar[i]]++; // at the key ar[i] i.e. color, increment val so 2 socks of that 
                                // which means we have 2 socks of that color now 
        }
    }
    
    // now we have a map of which key and which sock, so return how many pairs we have
    int sum =0;
    
    // go thru map of colors, and see how many we have of each 
    for (int i =0; i<n;i++){
        
        if (sockLookup[ar[i]] == 2){
            sum++;
        }
    }
    return sum;
    
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string ar_temp_temp;
    getline(cin, ar_temp_temp);

    vector<string> ar_temp = split_string(ar_temp_temp);

    vector<int> ar(n);

    for (int i = 0; i < n; i++) {
        int ar_item = stoi(ar_temp[i]);

        ar[i] = ar_item;
    }

    int result = sockMerchant(n, ar);

    fout << result << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
