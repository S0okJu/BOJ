#include<iostream>
using namespace std;

int w[101]; // 무게
int v[101]; // 가치
int dp[101][100001];
int main(){
    int N, K;
    cin >> N >> K;

    for(int i = 1 ; i <= N;i++){
        cin >> w[i]>> v[i];
    }
    
    for(int i = 1 ; i<=N;i++){
        for(int j = K; j>=1;j--){
            if(j-w[i]>=0){ // 물건을 넣을 수 있다면?
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i]);

            }
            else{ // 물건을 넣을 수 없다면?
                dp[i][j] = dp[i-1][j];
            }
        }
    }
    cout << dp[N][K];

    return 0;
}