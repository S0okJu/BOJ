#include<iostream>
#include<algorithm>
#include<stack>   
#include<string>
using namespace std;

bool areFriends[51][51] = {false,};
int dp[51][51];
int main(){
    int N;
    int ans = 0;
    cin >> N;

    for(int i = 0 ; i < N;i++){
        string input;
        cin >> input;
        for(string::size_type j = 0 ; j< input.size();j++){
            if(input[j]=='Y') areFriends[i][j] = true;
            else areFriends[i][j] = false;
        }
    }
   
    for(int i=0; i<N; i++){
        for(int j=0; j<N; j++)
        dp[i][j] = 1e9;
    }

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
                    // cout << dp[i][j]<<" "<<dp[i][k]<<" "<<dp[k][j]<<'\n';
                    dp[i][j] = dp[i][k] + dp[k][j];
                    // cout << "("<<i<<","<<j<<")"<<"="<< "("<<i<<","<<k<<")"<<"+"<< "("<<k<<","<<j<<")"<<'\n';
                    
                }
            }
        }
    }

    for(int i = 0 ; i < N;i++){
        int cnt = 0;
        for(int j = 0 ; j < N ; j++){
            if(i==j) continue;
            // 정점간의 거리가 2이하인 경우 
            if(dp[i][j]<=2){
                cnt+=1;
            }
        }
        cout << '\n';
        if(cnt > ans) ans = cnt;
    }
    cout << ans;

    return 0;
}