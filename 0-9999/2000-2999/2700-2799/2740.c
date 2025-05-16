#include<stdio.h>

int main(){
    int N, M, K;

    scanf("%d",&N );
    scanf("%d",&M );
    int A[N][M];
    for(int i = 0 ; i < N; i++){
        for(int j = 0 ; j < M; j++){
            scanf("%d",&A[i][j]);
        }
    }

    scanf("%d %d",&M,&K );
    int B[M][K];
    for(int i = 0 ; i < M; i++){
        for(int j = 0 ; j < K; j++){
            scanf("%d",&B[i][j]);
        }
    }

    for(int i = 0 ; i < N ;i++){
        for(int j = 0 ; j < K;j++){
            int tmp = 0;
            for(int k = 0 ; k < M;k++){
                tmp += A[i][k] * B[k][j];
            }
            printf("%d ",tmp);

        }
        printf("\n");
    }
    return 0;
    

}