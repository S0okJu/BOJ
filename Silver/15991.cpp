#include<iostream>
using namespace std;
//dp[i][j] = i의 숫자를 만들때 마지막에 j의 숫자를 사용하는 경우 
long long int dp[100001];
const long long int mod = 1e9+9;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;
    
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 2;
    dp[4] = 3;
    dp[5] = 3;
    dp[6] = 6;
    
    for(int i = 0 ; i < T; i++){
        int input;
        cin >> input;
        if(input>=7){
            for(int j = 7; j<=input;j++){
                dp[j] = (dp[j-2]+dp[j-4]+dp[j-6])%mod;
            }
        }

        cout<< dp[input]<<'\n';
    }


    return 0;
}