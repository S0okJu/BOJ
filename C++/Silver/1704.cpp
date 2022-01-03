#include<iostream>
#include<math.h>
#include<vector>
using namespace std;

vector<long long int> dp;

int main(){
    int a;
    cin >> a;
    vector<long long int> dp(a+1);

    dp[1] = 1;
    dp[2] = 3;
    int i = 3;
    int j;
    while(true){
        if((i+j-1)==a)break;
        for(j = 1;j<i-1;j++){
            dp[i+j-1] = dp[i-1] + dp[j];
        }
        i++;
        
    }
    cout <<dp[a];

    return 0;
}