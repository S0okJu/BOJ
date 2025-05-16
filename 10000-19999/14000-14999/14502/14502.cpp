#include<iostream>
using namespace std;

int dp[3][100001];
int sticker[2][100001];

int max(int a, int b, int c){
    int value = a > b?a:b;
    value = value > c ? value:c;

    return value;
}

int main(){
    int n;
    cin >> n;
    for(int k = 0 ; k < n ;k++){


        int NUM;
        cin >> NUM;
        for(int i = 0 ;i < 2;i++){
            for(int j = 0; j<NUM;j++){
                cin >> sticker[i][j];
            }
        }
        dp[0][0] = sticker[0][0];
        dp[1][0] = sticker[1][0];
        dp[2][0] = 0;
        
        for(int i = 0; i <NUM;i++){
            // 이전 스티커가 윗줄에 있는 경우
            dp[0][i] = max(dp[1][i-1],dp[2][i-1],0) + sticker[1][i];
            // 이전 스티커가 아랫줄에 있는 경우
            dp[1][i] = max(dp[2][i-1],dp[0][i-1],0) + sticker[0][i];
            // 아무런 변화가 없는 경우
            dp[2][i] = max(dp[0][i-1],dp[1][i-1],dp[2][i-1]);    
        }

        cout << max(dp[0][NUM-1],dp[1][NUM-1],dp[2][NUM-1])<<'\n';

    }


    


    return 0;
}
