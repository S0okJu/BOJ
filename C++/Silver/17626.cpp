#include<iostream>
#include<algorithm>
#include<cmath>
#include <vector>
using namespace std;

vector<int> dp(50001, 0x7f7f7f7f); // 최댓값으로 초기화..

int main(){
    int N;
    int Num=1;
    int count = 0;

    cin >> N;


    for(int i = 1; i <= N ;i++){
        if((int)sqrt(i)*(int)sqrt(i) == i){
            dp[i]=1;
        }
        else{
            for(int j = 1; j <=(int)sqrt(i);j++){
                dp[i]=min(dp[i],dp[j*j]+dp[i-j*j]);
            }
        }

    }
    cout << dp[N];
}