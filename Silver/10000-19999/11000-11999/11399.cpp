#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int dp[1001];

int main(){
    int T;
    vector<int> line;
    cin >> T;

    for(int i = 0 ; i < T; i++){
        int a;
        cin >> a;
        line.push_back(a);
    }

    sort(line.begin(),line.end());
    dp[1] = line[0];
    for(int i = 2 ; i <= T;i++){
        dp[i] = dp[i-1]+(dp[i-1]-dp[i-2]+line[i-1]);
        /*
        dp[1] = 1
        dp[2] = 1 + (1+2)
        dp[3] = 1 + (1+2) + (1+2+3)
        (1 + 2)을 이용해야 하므로 dp[i-1]-dp[i-2]을 통해 중복을 제거하면 
            원하는 정보를 얻을 수 있다.
        */
    }
    cout<<dp[T];
    return 0;
}