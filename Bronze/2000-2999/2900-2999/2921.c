#include<stdio.h>

int main(){
    int N;
    int sum = 0;
    scanf("%d",&N);

    for(int i = 0 ; i <= N;i++){
        for(int j = i; j<=N;j++){
            sum+=(i+j);
        }
    }

    printf("%d",sum);
    
    return 0;
    
}