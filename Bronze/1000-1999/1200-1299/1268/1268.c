#include<stdio.h>

int studClass[1001][5]; // 입력값 
int student[1001][1001]; // N * N 행렬값 
int main(){

    int N;
    scanf("%d",&N);

    for(int  i = 0 ; i< N;i++){
        for(int j = 0 ; j < 5;j++){
            scanf("%d",&studClass[i][j]);  
        }
    }

    for(int j = 0; j < 5;j++ ){
        for(int i = 0 ; i < N ;i++){
            for(int k = i+1 ;k<N;k++){
                if(studClass[i][j]==studClass[k][j]){
                    student[i][k]=1;
                    student[k][i]=1;
                }
            }
        }
    }

    int max =-1;
    int maxStud=0;
    for(int i = 0 ; i< N;i++){
        int cnt = 0;
        for(int j = 0 ; j < N;j++){
            if(student[i][j]==1){
                cnt++;
            }
        }
        if(cnt > max){
            max = cnt;
            maxStud = i+1;
        }
    }
    printf("%d",maxStud);
    return 0;
    
}