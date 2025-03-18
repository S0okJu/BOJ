#include<iostream>
#include<algorithm>
using namespace std;

int dp[100001]={0};
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int n;

    cin >> n;
    if(n==1||n==3){
        cout << -1;
        return 0;
    }

    dp[1] = 0; 
    dp[2] = 1; // 2을 1개 사용
    dp[3] = 0;
    dp[4] = 2; // 2 2개 사용 
 

    for(int i = 5; i <= n;i++){
        dp[i] = dp[i-2]+1; 
        // 2만 사용하는 경우
        //  5의 배수가 아닌 2의 배수는 무조건 2만 사용해야한다. 

        if(i%5==0){
            dp[i] = min(dp[i],dp[i-5]+1);
            // 최소(2를 무조건 사용하는 경우, 5를 무조건 사용하는 경우 )
        }

    }

    cout << dp[n];
    return 0;

}