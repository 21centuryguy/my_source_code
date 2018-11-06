#include <iostream>

int main()
{
	int count = 0;
	do
	{
		std::cout<<"Count = "<<count<<"\n";
		count ++;
	}while(count < 5);

	int otherCount = 6;
	do
	{
		std::cout<<"othercount = "<<otherCount<<"\n";
		otherCount++;
	}while(otherCount < 5);

	return 0;
}
