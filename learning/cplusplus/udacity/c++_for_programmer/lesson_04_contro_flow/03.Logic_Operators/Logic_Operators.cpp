
#include<iostream>
#include<string>

int main()
{
    int A = 5;
    int B = 4;
    int C = 5;
    int D = 0;
    
    std::string TorF[] = {"False", "True"};
    
    //The && operator
    std::cout<<"A("<<A<<") == C("<<C<<") is "<<TorF[A==C];
    std::cout<<"\n(B("<<B<<") == D("<<D<<")) is "<<TorF[B==D]; 
    std::cout<<"\n(B("<<B<<") > D("<<D<<")) is "<<TorF[B>D]; 
    //A true && false = false
    std::cout<<"\n\n(A("<<A<<") == C("<<C<<")) && (B("<<B<<") == D("<<D<<")) is "<<TorF[(A == C) && (B == D)];  
    //A true and true = true
    std::cout<<"\n(A("<<A<<") == C("<<C<<")) && (B("<<B<<") > D("<<D<<")) is "<<TorF[(A == C) && (B > D)];     

    //The || operator
    //A true || false = true
    std::cout<<"\n\n(A("<<A<<") == C("<<C<<")) || (B("<<B<<") == D("<<D<<")) is "<<TorF[(A == C) || (B == D)];  
    //A true || true = true
    std::cout<<"\n(A("<<A<<") == C("<<C<<")) || (B("<<B<<") > D("<<D<<")) is "<<TorF[(A == C) || (B > D)];  
    
    //The 'Not' operator
    std::cout<<"\n\nA("<<A<<") < B("<<B<<") is "<<TorF[A<B];
    std::cout<<"\n!(A("<<A<<") < B("<<B<<")) is "<<TorF[!(A<B)];
    
    std::cout<<"\n\nA("<<A<<") == C("<<C<<") is "<<TorF[A==C];
    std::cout<<"\n!(A("<<A<<") == C("<<C<<")) is "<<TorF[!(A==C)]<<"\n\n";
    
    return 0;
}