#include <iostream>
//#include <string>

int main()
{
	float in1, in2, op_result;
	char operation;
	//std::string operation;
	std::cout<<"Enter 1st number:\n";
	std::cin>>in1;
	std::cout<<"Enter 2nd number:\n";
	std::cin>>in2;
	std::cout<<"Enter the operation '+','-','*','/':\n";
	std::cin>>operation;
	std::cout<<"\n";

	switch(operation)
	{
		case('+'): std::cout<<in1<<"+"<<in2<<"= ";
			op_result = in1+in2;
			std::cout<<op_result<<"\n";
			break;
		case('-'): std::cout<<in1<<"-"<<in2<<"= ";
			op_result = in1-in2;
			std::cout<<op_result<<"\n";
			break;			
		case('*'): std::cout<<in1<<"*"<<in2<<"= ";
			op_result = in1*in2;
			std::cout<<op_result<<"\n";
			break;
		case('/'): std::cout<<in1<<"/"<<in2<<"= ";
			op_result = in1/in2;
			std::cout<<op_result<<"\n";
			break;
	}
	return 0;
}