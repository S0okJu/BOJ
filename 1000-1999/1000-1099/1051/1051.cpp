#include<iostream>
#include<queue>
#include<string>
#include<algorithm>
using namespace std;

int main(){
    int N, M;
    string square[51];//띄어쓰기 없이 입력받으므로 string으로 입력받는다.
    int ans = 1; // 정사각형이 존재하지 않을때 숫자 하나인 1이 최대값이므로..

    cin >> N >> M;
    int maxSquare = max(N,M); // 가로 세로 길이 중 큰 길이가 정사각형의 최대 길이가 된다.

    for(int i = 0 ; i < N;i++){
        cin >> square[i];
    }

    for(int i = 0 ; i < N;i++){
        for(int j= 0 ; j < M; j++){
            for(int k = 1 ; k< maxSquare;k++){
                if(i+k >= N || j+k >= M) continue; // 범위에 벗어나므로 다시 반복문을 돌린다.
                if(square[i][j] == square[i+k][j]&square[i+k][j] == square[i][j+k] &&square[i][j+k]==square[i+k][j+k]){
                    ans = max(ans,(k+1)*(k+1));
                }
            }
        }
    }
    cout << ans;

    return 0; 
}