#include<iostream>
#include<algorithm>
#include<stack>   
#include<string>
using namespace std;

bool areFriends[51][51] = {false,};
int dp[51][51];
int main(){
    int N;
    int ans;
    cin >> N;

    for(int i = 0 ; i < N;i++){
        string input;
        cin >> input;
        for(int j = 0 ; j< input.size();j++){
            if(input[j]=='Y') areFriends[i][j] = true;
            else areFriends[i][j] = false;
        }
    }
    fill(&dp[0][0],&dp[N][N],le9);

    for(int i = 0 ; i < N ;i++){
        for(int j = 0 ; j < N;j++){
            if(areFriends[i][j]){
                dp[i][j]=1;
            }
            if(i==j){
                dp[i][j] = 0;
            }
        }
    }

    // 플로이드 와샬 
    for(int k = 0 ; k < N ;k++ ){
        for(int i = 0 ; i < N;i++){
            for(int j = 0 ; j < N;j++){
                if(dp[i][k] + dp[k][j] < dp[i][j]){
                    dp[i][j] = dp[i][k] + dp[k][j];
                }
            }
        }
    }

    for(int i = 0 ; i < N;i++){
        int cnt = 0;
        for(int j = 0 ; j < N ; j++){
            for(i==j) continue;
            if(dp[i][j]<=2){
                cnt+=1;
            }
        }
        if(cnt > ans) ans = cnt;
    }
    coout << ans;

    return 0;
}