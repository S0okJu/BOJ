#include<iostream>
#include<algorithm>
using namespace std;

int buidling[1001][3];
int dp[1001][3];


int main(){
    int T;
    cin >> T;
    for(int i = 1 ; i <= T;i++){
        cin>>  buidling[i][0] >>buidling[i][1]>>buidling[i][2];
    }
    
    dp[2][0] = buidling[2][0]+min(buidling[1][1], buidling[1][2]);
    dp[2][1] = buidling[2][1]+min(buidling[1][0], buidling[1][2]);
    dp[2][2] = buidling[2][2]+min(buidling[1][0], buidling[1][1]);

    for(int i = 3; i<=T;i++){
        //i번째 건물의 색이 R인 경우 = i-1 건물이 G,B 경우 중의 최솟값 + i번째 건물 비용 
        dp[i][0] = buidling[i][0]+min(dp[i-1][1],dp[i-1][2]); 

        //i번째 건물의 색이 G인 경우 = i-1 건물이 R,B 경우 중의 최솟값 + i번째 건물 비용
        dp[i][1] = buidling[i][1]+min(dp[i-1][0],dp[i-1][2]); 

        //i번째 건물의 색이 B인 경우 = i-1 건물이 R,G 경우 중의 최솟값 + i번째 건물 비용
        dp[i][2] = buidling[i][2]+min(dp[i-1][0],dp[i-1][1]); 
    }

    int ans = min(dp[T][0],min(dp[T][1],dp[T][2]));
    cout << ans;
    return 0;
}