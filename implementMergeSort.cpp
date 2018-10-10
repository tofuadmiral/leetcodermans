#include <iostream> 
#include <vector> 
using namespace std;


int main(){

    int arraySize;

    // ask the user for an array of numbers
    cout << "How big do you want your array to be? " << endl;
    cin >> arraySize;
    std::vector<int> v(arraySize, 0);

    cout << "Cool! Now input the numbers for that array" << endl;
    for(int i=0; i<arraySize; i++){
        cout << "Input number " << i << endl;
        cin >> v[i];
    }

    // print out array so user can be sure that it's what they want
    // first, make an iterator
    for(int i =0; i<v.size(); i++){
        cout << "\n" << v[i] << endl;
    }

    // now actually sort the array

    void mergeSort(std::vector<int> array){
        if(array.size()==1){
            return array;
        }
        else{
            int mid = (leftbegin + rightend) / 2;
        }
    }


    return 0;
}