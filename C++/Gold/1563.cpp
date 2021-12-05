#include<iostream>
using namespace std;

const int divNum = 1000000;
int dp[1001][3][3]; // 날짜, 지각, 결석

int main(){
    int N;
    cin >> N;
    
    dp[1][0][0] = dp[1][1][0] = dp[1][0][1] =1;

    for(int i =2 ; i <=N;i++){
        dp[i][0][0] = (dp[i-1][0][0]+dp[i-1][0][1]+dp[i-1][0][2])%divNum;
        dp[i][0][1] = (dp[i-1][0][0])%divNum;
        dp[i][0][2] = (dp[i-1][0][1])%divNum;
        dp[i][1][0] = (dp[i-1][0][0]+dp[i-1][0][1]+dp[i-1][0][2]+dp[i-1][1][0]+dp[i-1][1][1])%divNum;
        dp[i][1][1] = (dp[i-1][1][0])%divNum;
        dp[i][1][2] = (dp[i-1][1][1])%divNum;
    }
    cout << (dp[N][0][0]+dp[N][0][1]+dp[N][0][2]+dp[N][1][0]+dp[N][1][1]+dp[N][1][2])%divNum;
    return 0;
}