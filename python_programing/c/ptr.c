#include <stdio.h>

int main(void){

    int x = 6; //整数型の変数定義
    int* a = &x;
    int *a = &x;

    printf("%p",a);

    return 0;
}