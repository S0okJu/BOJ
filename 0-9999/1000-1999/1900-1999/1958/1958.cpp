#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int dp[101][101][101];
int main(){
    string a,b,c;
    cin >> a >> b >> c;
    int lenA = a.length();
    int lenB = b.length();
    int lenC = c.length();

    for(int i = 1; i <=lenA;i++){
        for(int j = 1 ; j <=lenB;j++){
            for(int k = 1; k<=lenC;k++){
                if(a[i-1]==b[j-1] && b[j-1]==c[k-1]){
                    dp[i][j][k] = dp[i-1][j-1][k-1]+1;
                }
                else{
                    dp[i][j][k] = max(dp[i-1][j][k],max(dp[i][j-1][k],dp[i][j][k-1]));
                }
            }
        }
    }
    cout << dp[lenA][lenB][lenC];
    return 0;
}