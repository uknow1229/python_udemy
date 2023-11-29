# include <stdio.h>

int sum(int);

int main(void){
    int ans = sum(10);
    printf("%d",ans);
    return 0;
}

int sum(int n){
    if(n <= 0)
      return n;
    return n + sum(n-1);
}