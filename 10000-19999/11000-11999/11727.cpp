#include<iostream>
using namespace std;

int dp[1001];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    // 1. 마지막에 1 * 2 인 경우
    // 2. 마지막에 2 * 1이 2개인 경우
    // 3. 마지막에 2 * 2 하나 있는 경우 
    dp[0]= 0;
    dp[1] = 1;
    dp[2] = 3;

    for(int i = 3; i <=n;i++){
        dp[i]=((dp[i-1]%10007)+(dp[i-2]*2)%10007)%10007;
    }

    cout<<dp[n]%10007;
    return 0;
}