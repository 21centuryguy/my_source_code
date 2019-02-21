/*Goal: demonstrate use cases for the switch statement.*/

#include <iostream>

int main()
{
    int menuItem = 1;

    std::cout<<"What is your favorite winter sport?: \n";
    std::cout<<"1.Sking\n2: Sledding\n3: Sitting by the fie";
    std::cout<<"\n4.Dringking hot chocolate\n";
    std::cout<<"\n\n";

    switch(menuItem)
    {
        case(1): std::cout<<"Sking?! Sounds dangerous!\n";
            break;
        case(2): std::cout<<"Sledding?! Sound like work!\n";
            break;
        case(3): std::cout<<"Sitting by the fie?! Sounds warm!\n";
            break;
        case(4): std::cout<<"Hot chocolate?! Yum!\n";
            break;
        default: std::cout<<"Enter a valid menu item";

    }

    char begin;
    std::cout<<"\n\nWhere do you wnat to gegin?\n";
    std::cout<<"B. At the beginning?\nM. At the middle?";
    std::cout<<"\nE. At the end?\n\n";
    begin = 'M';

    switch(begin)
    {
        case('B'): std::cout<<"Once upon a time there wat a wolf.\n";
        case('M'): std::cout<<"The wolf hurt his leg\n";
        case('E'): std::cout<<"The wolf lived happily everafter\n";
    }
    return 0;

}