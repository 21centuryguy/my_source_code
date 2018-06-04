/*GOAL: Practice writing to the console and learn 
**the variables types available in C++
**Print the sizes of each variable to the console.
**Print them in the following order:
**int, short, long, char, float, double, bool
**
**Use the command sizeof(variable type) ie: sizeof(int)
*/

 #include <iostream>

int aaa = 2109765556;

 int main() {
     std::cout << sizeof(aaa);
     std::cin.ignore();
     return 0;
 }  
