#include <iostream>

int main(int argc, const char * argv[]) {
    
    unsigned int a, b, c;
    unsigned num=0;
    
    std::cin>>a>>b>>c;

    if(b >= c)
        std::cout << "-1";
    else{
        num = (a / (c-b)) + 1;
        std::cout<<num;
    }
}