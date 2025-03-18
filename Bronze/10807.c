#include<stdio.h>

int num[101];

int main()
{
    int N;
    int ans;
    int cnt = 0;
    scanf("%d",&N);

    for(int i = 0 ; i<N;i++){
        scanf("%d ",&num[i]);
    }

    scanf("%d",&ans);
    for(int i = 0 ; i<N;i++){
        if(num[i]==ans) cnt++;
    }
    printf("%d",cnt);
    return 0;
}