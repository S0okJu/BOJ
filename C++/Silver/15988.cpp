#include<iostream>
using namespace std;

long long int dp[1000001]={0,1,2,4};
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T;
    long long int input;

    cin >> T;
    for(int i = 0 ; i < T; i++){
        cin >> input;

        for(int j =4;j<=input;j++){
            dp[j]= (dp[j-3]+dp[j-2]+dp[j-1])%(long long int)(1e9+9);
        }
        cout << dp[input]<<'\n';
    }

    return 0;
}