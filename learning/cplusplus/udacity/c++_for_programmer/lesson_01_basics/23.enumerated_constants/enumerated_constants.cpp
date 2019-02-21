/*Enum example*/

#include <iostream>

using namespace std;

int main()
{
    //define MONTHS as having 12 possible values
    enum MONTHS {Jan, Feb, Mar, Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec};
    
    //define bestMonth as a variable type MONTHS
    MONTHS bestMonth;
    MONTHS worstMonth;    
    
    //assign bestMonth one of the values of MONTHS
    bestMonth = Jan;
    worstMonth = Apr;
    
    //now we can check the value of bestMonths just 
    //like any other variable
    if(bestMonth == Jan)
    {
        cout<<"I'm not so sure January is the best month\n";
    }
    
    if(worstMonth == Apr)
    {
        cout<<"I'm so sure April is the worst month\n";
    }
    return 0;
}
