#include<stdio.h>
#include<stdlib.h>

int main(){
    int T;
    
    scanf("%d",&T);
    for(int i = 0 ; i< T; i++){
        int num;
        int coinArray[4]={0,};
        scanf("%d",&num);

        coinArray[0] = num/25;
        num%=25;
        coinArray[1]=num/10;
        num%=10;
        coinArray[2]=num/5;
        coinArray[3]=num%5;

        printf("%d %d %d %d \n",coinArray[0],coinArray[1],coinArray[2],coinArray[3]);
    }

    return 0;

}