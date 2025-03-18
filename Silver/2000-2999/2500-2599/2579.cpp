#include<iostream>
#include<algorithm>
using namespace std;

int steps[301];
int dp[301];

int main(){
    int n;

    cin >> n;

    for(int i = 1 ; i <= n;i++){
        cin >> steps[i];
    }

    dp[1] = steps[1];
    
    for(int i = 2; i <=n;i++){
        dp[i] = max(dp[i-3]+steps[i-1], dp[i-2])+steps[i];
        // 1칸 2칸인 경우, 2칸인 경우의 최대값에서 현재 계단 수를 더한다. 
    }
    cout << dp[n];
    return 0;

}