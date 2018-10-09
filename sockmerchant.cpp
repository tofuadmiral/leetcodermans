#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the sockMerchant function below.
int sockMerchant(int n, vector<int> ar) {
    // ar is a vector, dynamically resizing array. n is the number of elements we have
    // ar is the socks data
    // let's make a map, key is the sock color, value is the number of those socks
    std::map<int, int> sockLookup;
    for (int i =0; i<n;i++){
        if(std::map::count(ar[i]) == 0){
            // key isn't in the map, so insert it
            sockLookup.insert(std::pair<int, int>(ar[i], 1)); // key is color, val = how many
        }
        else { // this means key is in it
            sockLookup[ar[i]]++; // at the key ar[i] i.e. color, increment it 
        }
    }
    // now we have counts, so return how many pairs we have
    int sum =0;
    for (int i =0; i<n;i++){
        // go thru array, lookup, and if val ==2 then add to sum 
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
