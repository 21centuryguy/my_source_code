/*The goal of this quiz is to practice writing and reading files.
**Read the contents of input.txt and then write to it. 
**
**We are using input.txt as our file. This is not an ideal
**situation, because when we write to it, we cannot
**see the changes. We can manually write in input.txt and
**we can also use the program to write to the file. 
**Then we can read what we wrote using our program.
**
**Your assignment for this quiz**
**Change the contents of the file called input.txt
**Change the ifstream and ofstream to fstream

*/
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
    string line;
    
    ofstream myfileO;
    myfileO.open("input.txt", ios::app);
    //myfileO.open("input.txt");
    
    if (myfileO.is_open())
    {
        myfileO << "\nI am adding a line.\n\n";
        myfileO << "I am adding another line.\n";
        myfileO.close();
    }
    else cout << "Unable to open file for writing";
    
    ifstream myfileI;
    myfileI.open("input.txt");
    if (myfileI.is_open())
    {
        while ( getline (myfileI,line) )
        {
            cout << line << '\n';
        }
        myfileI.close();
    }
    else cout << "Unable to open file for reading";
    
    return 0;
}
