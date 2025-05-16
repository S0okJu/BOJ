#include<cstdio>

char original[][6]={
    "  *  ",
    " * * ",
    "*****" 
};
char shape[3500][6500];

void solve(int y, int x, int n){
    if(n==1){
        for(int i = 0 ; i < 3;i++){
            for(int j = 0 ; j < 5; j++){
                shape[y+i][x+j] = original[i][j];
            }
        }
        return ;
    }
    solve(y, x+3*n/2,n/2);
    solve(y+3*n/2, x,n/2);
    solve(y+3*n/2, x+3*n,n/2);
}
int main(){
    int n;
    scanf("%d", &n);
    solve(0, 0,n/3);
    for(int i=0;i<n;i++){
        for(int j=0;j<2*n-1;j++){
            printf("%c", shape[i][j] == '*' ? '*' : ' ');
        }
        printf("\n");
    }
    return 0;
}