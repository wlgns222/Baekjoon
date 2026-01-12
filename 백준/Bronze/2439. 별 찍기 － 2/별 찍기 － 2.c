#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    
    for(int i = 0; i < num; i++){  // 0부터 num-1까지 증가
        for(int j = 0; j < num; j++){
            if(j < num - i - 1)  // 오른쪽 정렬을 위한 공백
                printf(" ");
            else
                printf("*");
        }
        printf("\n");
    }
    
    return 0;
}
