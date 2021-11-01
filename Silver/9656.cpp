#include<iostream>
#include<algorithm>
using namespace std;

int dp[1001];
int main(){
    int N;
    int checkPerson ;
    cin >> N;
    dp[0] = N;
    for(int i = 1 ; i <= N;i++){
        if(dp[i] >=3){
            dp[i] = dp[i-1] -3;
        }
        else dp[i] = dp[i-1]-1;

        if(dp[i]==0){
            checkPerson = i;
            break;
        }
    }

    if(checkPerson%2 == 1){
        cout << "CY";
    }
    else cout << "SK";
}