#include <stdio.h>

int sum(int,int); //宣言

int main(void){

    int ans;
    ans = sum(2,3);
    printf("%d",ans);
    return 0;
}

int sum(int a,int b){
    int ans;
    ans = a+b;
    return ans;

    //return a+b;
}
