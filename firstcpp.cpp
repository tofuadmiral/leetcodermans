#include<iostream>

// we're gonna use the std output stream
using namespace std;


// now let's make a class

class Cars 
{
    public: 

    // data members
    string carname;
    int maxspeed;
    string make;

    // member functions
    void printCar(){
        cout << "this car is a " << make << " named " << carname << " with a max speed of " << maxspeed << endl;
    }
};


// this is our main function with returns an integer
int main() // takes no parameters
{
            cout<<"hello world\n";
            cout << "\n";
            Cars car1;
            car1.carname = "sonata";
            car1.make = "hyundai";
            car1.maxspeed = 100;
            car1.printCar();
            return 0;
}
