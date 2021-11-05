#include <iostream>
const int MOD = 1e9+9;
using namespace std;
 
int dp[100001][2];
 
 
int main() {
    cin.tie(NULL); cout.tie(NULL);
    ios::sync_with_stdio(false);
 
    dp[1][0] = 1;
    dp[2][0] = 1;
    dp[2][1] = 1;
    dp[3][0] = 2;
    dp[3][1] = 2;

    for (int i = 4; i <= 100000; i++) {
        dp[i][0] = ((dp[i - 1][1] + dp[i - 2][1]) % MOD + dp[i - 3][1]) % MOD;
        dp[i][1] = ((dp[i - 1][0] + dp[i - 2][0]) % MOD + dp[i - 3][0]) % MOD;
    }
    int T, N;
    cin >> T;
    while (T--) {
        cin >> N;
        cout << dp[N][0] << ' ' << dp[N][1] << '\n';
    }
 
    return 0;
}
