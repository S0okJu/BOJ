#include<stdio.h>
#include<stdlib.h>
int main(){
    int N;
    scanf("%d",&N);
    int*square = (int*)malloc(sizeof(int)*(N+1));
    long long int area = 0;

    square[0] = 0;
    square[1] = 1;
    for(int i = 2; i <=N;i++){
        square[i] = square[i-1]+square[i-2];
    }

    area = (square[N]*2) + (square[N]+square[N-1])*2;
    printf("%lld",area);
    free(square);
    return 0;
}