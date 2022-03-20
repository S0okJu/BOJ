#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int L[21];
int J[21];
int dp[101];

int main(){

    int N;
    cin >> N;

    for(int i = 1 ; i <= N;i++){
        cin >> L[i];
    }
    for(int i = 1 ; i <= N;i++){
        cin >> J[i];
    }
    
    for(int i =1; i<=N ;i++){
        for(int j=100 ; j>L[i];j--){
            dp[j] = max(dp[j],dp[j-L[i]]+J[i]);
        }
    }

    cout << dp[100];
        
    return 0;
}