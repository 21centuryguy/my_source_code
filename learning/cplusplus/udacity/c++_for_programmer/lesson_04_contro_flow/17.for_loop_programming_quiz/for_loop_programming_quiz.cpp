/*Write a program that asks a user for five numbers.
**Print out the sum and average of the five numbers.
*/

#include <iostream>

int main()
{
		float a, sum=0, average;
		for(int i=0; i<5; i++)
		{
			std::cout<<"Input a number :\n";
			std::cin>>a;
			sum = a + sum;
			// std::cout<<a<<"\n";
			// std::cout<<sum<<"\n";
			// average = sum/i+1;
		}
		average = sum / 5;
		std::cout<<"sum : "<<sum<<"\n";
		std::cout<<"average : "<<average<<"\n";
	return 0;
}
