#include <stdio.h>

int main(int argc, const char * argv[]) {
    
    int num1, num2, o, t, h;
    scanf("%d %d", &num1, &num2);
    
    o = num2 % 10;
    t = (num2 % 100) / 10;
    h = num2 / 100;
    
    printf("%d \n", num1*o);
    printf("%d \n", num1*t);
    printf("%d \n", num1*h);
    printf("%d \n", num1*num2);
}