#include<iostream>
#include<algorithm>
using namespace std;

int dp[1001];
int main(){
    int N;
    int *money = new int[N+1];
    
    cin >> N;
    for(int i = 1 ; i <= N ;i++){
        cin >> money[i];
        
    }
    dp[1] = money[1];
    for(int i = 2 ; i <=N;i++){
        for(int j = 1 ;j <= i;j++){
            dp[i] = max(dp[i],money[j]+dp[i-j]);
        }
    }
    cout << dp[N];

    delete[] money;
}











