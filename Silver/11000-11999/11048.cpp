#include<iostream>
#include<algorithm>
using namespace std;

int candy[1001][1001];
int dp[1001][1001];

int main(){
    int N, M;

    cin >> N >> M;

    for(int i = 1; i<=N;i++){
        for(int j = 1; j<=M;j++){
            cin >> candy[i][j];
        }
    }
    
    for(int i = 1; i<=N; i++) {
        for(int j = 1; j<=M; j++) {
            dp[i][j] = candy[i][j] + max(max(dp[i][j-1], dp[i-1][j]) , dp[i-1][j-1]);
        }
    }

    cout << dp[N][M];


    return 0;
}