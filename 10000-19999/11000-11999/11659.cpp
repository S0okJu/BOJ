#include<iostream>
using namespace std;

int arr[100001];
int dp[100001]; // dp = 숫자들의 합 

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N, M;
    cin >> N >> M;

    for(int i = 1 ; i <= N;i++){
        cin >> arr[i];
        dp[i] += (dp[i-1] + arr[i]); 

    }
    for(int j = 0 ; j < M; j++){
        int a, b;
        int ans = 0;
        cin >> a >> b;
        
        ans = dp[b]-dp[a-1]; // a의 범위가 포함되므로 dp[a-1]을 빼줘야한다. 

        cout << ans<<'\n';

    }
    return 0;
}