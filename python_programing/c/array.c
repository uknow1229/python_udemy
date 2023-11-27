#include <stdio.h>

int main(void){
    // 変数
    int age = 20; //整数
    printf("I'm %d. \n");

    char name[100] = "Ryota";
    printf("My name is %c", name);

    // 配列
    int nums[5] = {4,5,6,7,2};
    printf("%d\n",nums[2]);

    // 構造体
    struct animal{
        int id;
        char name[100];
        struct animal*enemy;
    };

    struct animal animals[3] =
    {
      {1,"Buffalo",NULL},
      {2,"Dolphin",&animals[2]},
      {3,"Goat",&animals[1]}
    };

    printf("%d\n",animals[0].id);


    return 0;
}