#include<stdio.h> 

int main(){
    /*
    나머지 연산자 사용(%4)
    - 0:짝(2)
    - 1:짝,홀(0)
    - 2:홀(1)
    - 3:짝,홀(0)
    */

   int n;
   scanf("%d",&n);
   
    if(n%4 == 1 || n%4 == 3){
        printf("0");
    }
    else if(n%4==0){
        printf("2");
    }
    else{
        printf("1");
    }
    return 0;
}