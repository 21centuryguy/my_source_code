#include<iostream>

int main()
{
	int a = 65;
	char charA = 65;
	char charB = 'B';
	float answer = 0;
	int integer_answer = 0;
	float floatNumber_answer = 0;
	char charB_answer = 0;
	char charC1 = 67;
	char charC2 = 67;
	char charC3 = 67;
	int integer = 80;
	float floatNumber = 0.0;

	std::cout<<"a = "<<a<<"\n";
	std::cout<<"charA = "<<charA<<"\n";
	std::cout<<"charB = "<<charB<<"\n";

	//We can assign an integer to a float
	floatNumber = integer;
	std::cout<<"integer = "<<integer<<"\n\n";
	std::cout<<"floatNumber = integer = "<<floatNumber<<"\n";

	//We can assign a char to a float
	floatNumber = charB;
	std::cout<<"floatNumber = charB = "<<floatNumber<<"\n";

	//check the type
	integer_answer = integer/4;
	std::cout<<"answer = integer("<<integer<<")/4 = "<<integer_answer<<"\n";

	floatNumber_answer = floatNumber/4;
	std::cout<<"answer = floatNumber("<<floatNumber<<")/4 = "<<floatNumber_answer<<"\n";

	charB_answer = charB/4;
	std::cout<<"answer = charB("<<charB<<")/4 = "<<charB_answer<<"\n";

	//But assigning a float to a char doesn't quite work
	charC1 = integer_answer;
	std::cout<<"charC1 = answer ="<<charC1<<"\n";
	//But assigning a integer to a char doesn't quite work
	charC2 = floatNumber_answer;
	std::cout<<"charC2 = answer ="<<charC2<<"\n";
	//But assigning a char to a char does work
	charC3 = charB;
	std::cout<<"charC3 = answer ="<<charC3<<"\n";

	//assigning a float to an interger, reslts in the float being truncated
	integer = floatNumber_answer;
	std::cout<<"integer = floatNumber = "<<integer<<"\n";
	return 0;

}