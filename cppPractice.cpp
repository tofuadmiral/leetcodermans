#include <iostream>
#include <vector>
#include <map> 
using namespace std;

/*
    A Lonely Pixel is the only bright pixel in its row and column. 

    Example input (assuming "1" represents white): 
    00100
    00001
    01001 
    00010 
*/

// function declaration, definition is below
vector<pair <int,int> >lonelyPixelFinder(vector<vector<int> >input);

// main function 
int main()
{   
    // initialize input vector (as per the example given)
    vector<vector<int> >input;
    vector<int> row0={0,0,1,0,0};
    vector<int> row1={0,0,0,0,1};
    vector<int> row2={0,1,0,0,1};
    vector<int> row3={0,0,0,1,0};
    input.push_back(row0);
    input.push_back(row1);
    input.push_back(row2);
    input.push_back(row3);

    // call our function, lonelyPixelFinder()
    vector<pair<int, int> >returnValues=lonelyPixelFinder(input);

    // this is where we print our values 
    for(int i=0; i<returnValues.size(); i++){
        cout << returnValues[i].first << ", " << returnValues[i].second << endl;
    }
    return 0;

}

// this is our lonelyPixelFinder() function definition 
vector<pair<int,int> >lonelyPixelFinder(vector<vector<int> > input){
    
    // create our return vector
    vector<pair<int, int> > returnPairs;
    
    // create our map for items that are row-lonely
    // --key is the row it appears it --value is the column
    map<int,int>rowMap;
    
    // loop through rows and find if a bright is row-lonely
    // row-lonely means the only bright in its row, so add it to the map
    for (int i=0; i<input.size(); i++){
        int numBrights=0;
        int colOfBright=0;
        for(int j=0; j<input[0].size(); j++){
            if(input[i][j]==1){
                numBrights++;
                colOfBright=j;
            }
        }
        if(numBrights==1){rowMap[i]=colOfBright;}
    }

    // now we have all the row-lonely pixels. 
    // A pixel is overall lonely if it's also the only bright in its column
    // so loop through cols, find if pixel col-lonely
    //      if it is, check if that row has corresponding entry as row lonely
    //          if it does, add to our return map
    for(int i=0; i<input[0].size(); i++){ // here, i refers to column number
        int numBrights=0;
        int rowOfBright=0;
        for(int j=0; j<input.size(); j++){ // here, j refers to row number
            if(input[j][i]==1){
                numBrights++;
                rowOfBright=j;
            }
        }
        if(numBrights==1 && rowMap.find(rowOfBright)!=rowMap.end()){
            // this means it's a row lonely (in row lonely map) & col lonely pixel
            returnPairs.push_back(make_pair(rowOfBright,i)); // add to our return vector
        }
    }
    return returnPairs;
}


/*
    TIME COMPLEXITY
    findLonelyPixels() takes an input of size E (n rows * m columns)
    it then
        - iterates through every row, then checks over it's columns = (O(E)
        - adds relevant rows to our map (O(1)), adding to dictionary
        - iterates through every col, then checking over it's rows = O(E)
        - if it's the only bright in its col, checks if that row/col combination 
          also exists in the dictionary, and if it does, adds to return vector
          (O(1))

        OVERALL: O(E), where E is the input size (linear time complexity)

    SPACE COMPLEXITY
        - dictionary which stores brights that are the row-lonely
          worst case is max row-lonely brights = number of rows = O(n)
        - temp variables to store how many brights we've seen, which row/col we're at (O(1))



    Thanks for reading through this and for such a great interview :)
    Glad I could clarify some of my thoughts through this code. 
*/