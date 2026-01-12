
#include <iostream>
#include <string>

int main(int argc, const char * argv[]) {
    // insert code here...
    
    int num, r;
    std::cin >> num;
    std::string str;
    
    for(int i = 0; i < num; i++){
        std::cin >> r;
        std::cin >> str;
        for(char c : str){
            for(int j = 0; j < r; j++)
                std::cout << c;
        }
        std::cout << "\n";
    }
}
