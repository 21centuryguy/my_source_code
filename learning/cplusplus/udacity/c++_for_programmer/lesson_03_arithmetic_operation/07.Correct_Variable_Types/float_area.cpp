 #include <iostream>

     int main()
     {
          float width = 4.5;
          float height = 5.5;
          int integer_width = 0;
          int integer_height = 0;

          integer_width = width;
		  integer_height = height;          
          int area = width * height;
          std::cout << "area = " << area<<"\n";
          return 0;
     }