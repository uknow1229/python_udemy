int main(void){

  int a = 15;
  int b = 2;
  int c = 0;

  if(a<10){
    printf("under 10,");
  }else if(a){// 10<=a<15

  }
  else{
    printf("upper 10.");
  }

  int i = 0;

  while(i<100){
    printf("Hello\n");
    i = i + 1;
  }

  for(i=0; i<100; i++){
    printf("Hello\n");
  }
  
  for(int i = 0; i<100; i++){
      if(i==16){
        break; //今行っているloopを抜ける
        //continue; //行っているloopの現在の繰り返しを飛ばす
      }
      printf("%d",i);
  }
  return 0;
}

