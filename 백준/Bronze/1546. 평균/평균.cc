#include <iostream>

int main(int argc, const char * argv[]) {
    
    int num;
    std::cin >> num;
    double grade[num];
    for (int i = 0; i < num; i++)
        std::cin >> grade[i];
    
    double max = grade[0];
    for (int j = 1; j < num; j++) {
        if (max < grade[j])
            max = grade[j];
    }
    
    double ave = 0;
    for (int k = 0; k < num; k++) {
        grade[k] = grade[k] / max * 100;
        ave = ave + grade[k];
    }
    std::cout << ave/num ;
}