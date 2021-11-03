#include<iostream>
using namespace std;

int dp[1001][1001];
int mod = 1e9+9;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;

    dp[1][1]=dp[2][1]=dp[2][2]=dp[3][1]=dp[3][3]=1;
    dp[3][2] = 2;


    for(int i = 4; i<=1000;i++){
        for(int j = 1; j<=i;j++){
            dp[i][j] = ((dp[i-1][j-1]+dp[i-2][j-1])%mod+dp[i-3][j-1])%mod;
        }
    }

    for(int i = 0 ; i < T;i++){
        int n, m;
        cin >> n >> m;

        cout << dp[n][m]<<'\n';
    }
    return 0;
}