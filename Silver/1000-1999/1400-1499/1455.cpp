#include<iostream>
#include<string>
using namespace std;

int coin[101][101];

void reverse_coin(int n, int m){

    for(int i = n ; i>=0;i--){
        for(int j = m ;j >=0;j--){
            if(coin[i][j]==1){
                coin[i][j] = 0;
            }
            else{
                coin[i][j] = 1;
            }
        }

    }
}

int main(){
    int N, M;
    int cnt = 0;
    cin >> N >> M;

    for(int i = 0 ; i < N; i++){
        string a;
        cin >> a;
        for(int j = 0 ; j < M;j++){
            coin[i][j] = a[j]-'0';
        }
    }

    for(int i = N-1; i >=0; i--){
        for(int j = M-1; j>=0;j--){
            if(coin[i][j]==1){
                reverse_coin(i,j);
                cnt++;
            }
        }
    }

    cout << cnt;
    return 0;
}