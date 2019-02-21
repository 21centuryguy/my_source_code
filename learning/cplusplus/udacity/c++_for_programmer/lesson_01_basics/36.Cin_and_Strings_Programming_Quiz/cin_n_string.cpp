#include<iostream>
#include<string>

int main(){
    // set user info variables
    std::string name_user1;
    std::string address_user1;
    std::string tphonenumber_user1;
    std::string name_user2;
    std::string address_user2;
    std::string tphonenumber_user2;    
    
    // ask user info
    std::cout<<"Please, type name (user1) : \n";
    std::cout<<"Please, type address (user1) : \n";
    std::cout<<"Please, type phone Number (user1) : \n";
    std::cout<<"Please, type name (user2) : \n";
    std::cout<<"Please, type address (user2) : \n";
    std::cout<<"Please, type phone Number (user2) : \n";

    // get user info
    std::getline(std::cin, name_user1);
    std::getline(std::cin, address_user1);
    std::getline(std::cin, tphonenumber_user1);
    std::getline(std::cin, name_user2);
    std::getline(std::cin, address_user2);
    std::getline(std::cin, tphonenumber_user2);

    // print user info
    std::cout<<name_user1<<"\n";
    std::cout<<address_user1<<"\n";
    std::cout<<tphonenumber_user1<<"\n";
    std::cout<<name_user2<<"\n";
    std::cout<<address_user2<<"\n";
    std::cout<<tphonenumber_user2<<"\n";

    return 0;
}