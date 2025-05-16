#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int dp[1001][1001];
string a, b;
string ans[1001][1001];

void print(int i, int j){
    if(dp[i][j]==0)return;
    if(a[i-1]==b[j-1]){
        print(i-1,j-1);
        cout<<a[i-1];
    }
    else{
        dp[i-1][j]> dp[i][j-1]?print(i-1,j):print(i,j-1);
    }
}
int main(){

    int lenA, lenB;
    int ind = 1;
    cin >> a >> b;
    
    lenA = a.length();
    lenB = b.length();

    for(int i = 1; i <=lenA; i++){
        for(int j = 1; j<=lenB;j++){
            if(a[i-1]==b[j-1]){
                dp[i][j] = dp[i-1][j-1]+1;

            }
            else{
                dp[i][j] = max(dp[i-1][j],dp[i][j-1]);
            }

        }

    }
    cout << dp[lenA][lenB]<<'\n';
    print(lenA,lenB);

        
    return 0;
}