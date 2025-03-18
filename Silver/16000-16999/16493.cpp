#include<iostream>
#include<algorithm>
using namespace std;

int arr[21][2];
int dp[21][201];

int main(){
	int n, m;
	cin >> n >> m;

	for(int i = 1 ; i <= m;i++){
		cin >> arr[i][0] >> arr[i][1];
	}

	for(int i = 1 ; i <= m; i++){
		for(int j =0;j<=n;j++){
			if(j-arr[i][0]>=0){ // 해당 챕터를 읽는 경우
				dp[i][j] = max(dp[i-1][j-arr[i][0]]+arr[i][1],dp[i-1][j]);
			}
			else{ // 해당 챕터를 읽지 않는 경우
				dp[i][j] = max(dp[i-1][j],dp[i][j]);
			}
		}
	}
	cout << dp[m][n];

	return 0;
}