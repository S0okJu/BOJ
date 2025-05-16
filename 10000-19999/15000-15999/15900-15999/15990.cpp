#include<iostream>
using namespace std;
//dp[i][j] = i의 숫자를 만들때 마지막에 j의 숫자를 사용하는 경우 
long long int dp[100001][4];
const long long int mod = 1e9+9;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T;
    cin >> T;
    
    dp[1][1] = dp[2][2] = dp[3][1] = dp[3][2] = dp[3][3] = 1; // 초기값 설정 

    for(int j=4;j<=100000;j++){
        // 같은 숫자 2개 이상 중복이 불가능하므로 마지막에 1이 나올때 2,3만 나올 수 있다. 
        if((j-1)>=0){
            dp[j][1] = (dp[j-1][2]+dp[j-1][3])%mod;
        } 
        if((j-2)>=0){
            dp[j][2] = (dp[j-2][1]+dp[j-2][3])%mod;
        } 
        if((j-3)>=0){
            dp[j][3] = (dp[j-3][1]+dp[j-3][2])%mod;  
        }
    }
    for(int i = 0 ; i < T;i++){
        int input;
        cin >> input;
        cout <<(dp[input][1]+dp[input][2]+dp[input][3])%mod<<'\n';
    }


    return 0;
}

