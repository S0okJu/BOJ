#include<stdio.h>
#include <stdlib.h>


int main(void){
    int N;
    int lastN;
    int tmp = 0;
    scanf("%d",&N);

    lastN = (2*N)-1;
    tmp = lastN;
    for(int i=0;i<lastN/2;i++){
        for (int blank = 0 ; blank < i;blank++){
            printf(" ");
        }
        for(int star = tmp ; star >0;star--){
            printf("*");
        }
        tmp -=2;
        printf("\n");
    }
    tmp = 1;
    for(int i = lastN/2 ; i>=0;i-- ){
        for(int blank = 0 ; blank<i;blank++){
            printf(" ");
        }
        for(int star = tmp ; star >0;star--){
            printf("*");
        }
        tmp +=2;
        printf("\n");
    }
    return 0;


}