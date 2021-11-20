#include<iostream>
using namespace std;
int N, M, K;
int garden[51][51];


void dfs(int x, int y){
    if(x >= M || x <0 || y >= N || y <0||garden[x][y]==0) return;
    
    garden[x][y] = 0;
    dfs(x+1, y);
    dfs(x, y+1);
    dfs(x-1, y);
    dfs(x, y-1);
}

int main(){
    int T;
    cin >> T;

    while(T--){
        cin >> N >> M >> K;
        while(K--){
            int a, b;
            cin >> a >> b;
            garden[b][a]=1;

        }

        int cnt = 0;
        for(int i = 0 ; i < N ;i++){
            for(int j = 0 ;  j < M;j++){
                if(garden[j][i]==1){
                    dfs(j,i);
                    cnt++;
                }
            }
        }
        cout << cnt<<'\n';

    }
}