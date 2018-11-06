/*Goal: In the programming quiz, use a while loop to prompt
**the user to guess a target number. 
**Tell the user if the guess is too high or too low. 
**The user enters -1  or guesses the target number to end 
**the program.
*/

#include <iostream>
#include<sstream>

int main()
{
	//use 55 as the number to be guessed
	int target = 55;
	int guess = -1;
	do
	{
	    std::cout<<"Guess a number between 0 and 100: ";
	    std::cin>>guess;
	    std::cout<<guess<<"\n";

	   	if (guess > target)
	   	{
	   		std::cout<<"Too high"<<"\n";
	   	}

	   	else if ((guess < target) && ( 0 < guess ))
	   	{
	   		std::cout<<"Too low"<<"\n";
	   	}

	   	else if (guess == -1)
	   	{
	   		std::cout<<"Good bye!"<<"\n";
	   		break;
	   	}

	    else
	    {
	   		std::cout<<"bingo !"<<"\n";	        
	    }

	}while(guess != target);
            
    return 0;
}
