#include <stdio.h>

int main(int argc, const char * argv[]) {

    char c[1000000];
    int num = 1, i;
    
    for (i = 0; i < sizeof(c); i++) {
        scanf("%c", &c[i]);
        if (c[i] == '\n') {
            break;
        }
    }
    c[i] = '\0';
    
    if(c[0] == ' ')
        num -= 1;
    if(c[i-1] == ' ')
        num -= 1;
    
    for (int j = 0; j < i; j++) {
        if (c[j] == ' ')
            num++;
    }
    
    printf("%d", num);
}
