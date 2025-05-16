#include<stdio.h>
#include<stdlib.h>

int dp[100001];

int max(int a, int b){
    return a > b ? a :b;
}
int main(void){
    int N;
    int *value;
    int ans= -1001;
    scanf("%d",&N);
    value = (int*)malloc(sizeof(int)*N);
    
    for(int i = 0 ; i < N ;i++){
        scanf("%d",&value[i]);
    }
    
    for(int i = 1; i <= N;i++){

        dp[i]=max(dp[i-1]+value[i-1],value[i-1]);
        ans = max(ans, dp[i]);
        // printf("%d ",dp[i]);
    }
    
    printf("%d",ans);
    free(value);
    return 0;
}