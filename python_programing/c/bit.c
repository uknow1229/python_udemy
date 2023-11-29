#include <stdio.h>

int main(void){

  int a = 0x10; //0001 0000
  int b = 0x11; //0001 0001

  int ans;
  ans = a & b; //& -> and | -> or

  printf("%x\n",ans);
  printf("%x\n",b<<2); // << >> 右シフト 左シフト

  return 0;
}