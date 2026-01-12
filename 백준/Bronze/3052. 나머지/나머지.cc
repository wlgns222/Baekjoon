
#include <iostream>
//#include <string>

int main(int argc, const char * argv[]) {

    int num[10];
    for (int i=0; i < 10; i++) {
        std::cin >> num[i];
        num[i] = num[i] % 42;
    }

    int count = 0;
    for (int j = 0; j < 10; j++) {
        for(int k = j+1; k < 10; k++){
            if(num[j] == num[k]){
                num[k] = -1;
            }
        }
        if (num[j] != -1)
            count++;
    }
    std::cout<<count;
}