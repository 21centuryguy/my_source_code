#include <iostream>

int main()
{

	// get the value of variables
    int a = 54;
    int b = 544;
    int c = 5444;
    
    std::cout<<"a = "<<a<<"\n";
    std::cout<<"b = "<<b<<"\n";
    std::cout<<"c = "<<c<<"\n";
    
    // get the location of variables
    std::cout<<"address of a is at &a = "<< &a<<"\n";
    std::cout<<"address of b is at &b = "<< &b<<"\n";
    std::cout<<"address of c is at &c = "<< &c<<"\n";

    // dereferencing variables
    int * pointerToA = &a;
    int * pointerToB = &b;
    int * pointerToC = &c;

    std::cout << "pointerToA poinsts to " << * pointerToA << '\n';
    std::cout << "pointerToB poinsts to " << * pointerToB << '\n';
    std::cout << "pointerToC poinsts to " << * pointerToC << '\n';       
    
    return 0;
}