#include <stdio.h>

int main(void){
    int num1, num2;
    scanf("%d %d", &num1, &num2);

    printf("%.9f", (double)num1/num2);
}
