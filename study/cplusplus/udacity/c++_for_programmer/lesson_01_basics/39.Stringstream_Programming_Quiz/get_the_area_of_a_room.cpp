 #include <iostream>
 #include <string>
 #include <sstream>
 
 int main(){
     std::string length_text;
     std::string width_text;
     float length_num = 0;
     float width_num = 0;     
     float area = 0;     
     
     //get length and width
     std::cout<<"Enter the length of your room: \n";
     std::cout<<"Enter the width of your room: \n";
     std::getline(std::cin,length_text);
     std::getline(std::cin,width_text);
     
     //stirng -> number
     std::stringstream(length_text)>>length_num;
     std::stringstream(width_text)>>width_num;     
     
     //get and print the area of a room
     std::cout<<"the length of your room: "<<length_num<<"\n";
     std::cout<<"the width of your room: "<<width_num<<"\n";
     area = length_num*width_num;
     std::cout<<"The are of your room: "<<area;
     
     return 0;
 }