#include<iostream>
#include<queue>
#include<string>
#include<algorithm>
using namespace std;

int main(){
    int N, M;
    string square[51];
    int ans = 1;

    cin >> N >> M;
    int maxSquare = max(N,M);

    for(int i = 0 ; i < N;i++){
        cin >> square[i];
    }
    for(int i = 0 ; i < N;i++){
        for(int j= 0 ; j < M; j++){
            for(int k = 1 ; k< maxSquare;k++){
                if(i+k >= N || j+k >= M) continue;
                if(square[i][j] == square[i+k][j]&square[i+k][j] == square[i][j+k] &&square[i][j+k]==square[i+k][j+k]){
                    ans = max(ans,(k+1)*(k+1));
                }
            }
        }
    }
    cout << ans;

    return 0; 
}