#include<iostream>
using namespace std;

int arr[301][301];
int dp[301][301];


int main(){
    int N, M;
    int K;
    cin >> N >> M;

    for(int i = 1 ; i<= N;i++){
        for(int j = 1; j <= M;j++){
            cin >> arr[i][j];
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i][j];
        }
    }

    cin >> K;
    int i, j ,a ,b;
    for(int u = 0 ; u < K;u++){
        int sum;
        cin >> i >> j >> a >> b;
        sum = dp[a][b] - dp[i-1][b] - dp[a][j-1] + dp[i-1][j-1];
        cout << sum<<"\n";

    }
    

    return 0;

}