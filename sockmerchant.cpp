#include <bits/stdc++.h>

// if we include using namespace std, we don't have to write std::map all the time
using namespace std;

vector<string> split_string(string);

// Complete the sockMerchant function below.
int sockMerchant(int n, vector<int> ar) {
    
    // this is what we'll return at the end
    int sum = 0;
    
    // ar is a vector, dynamically resizing array. n is the number of elements we have
    // ar is the socks data
    
    // let's make a map, key is the sock color, val = number of pairs found
    std::map<int, int> sockLookup;
    
    // now loop through ar and add to the map
    for (int i=0; i<n; i++){
        sockLookup[ar[i]]++; // if it doesn't exist, initialized then incremented to 1
                            // if it does, then incremented to n+1
    }
    
    // now that we have all the sock values in the map, iterate through the map and add
    map<int, int>::iterator it; 
    for(it=sockLookup.begin(); it!=sockLookup.end(); it++){
        sum += (it->second)/2; // give it the val of the number of pairs in each key 
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
