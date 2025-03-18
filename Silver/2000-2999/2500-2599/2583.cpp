#include<iostream>
#include<queue>
#include<algorithm>
#include<vector>
using namespace std;

const int moveX[4] = {1, 0, -1, 0};
const int moveY[4] = {0, 1, 0, -1};

int map[101][101];
bool visited[101][101];

int main(){
    int M, N, K;
    int cnt = 0;
    vector<int> ans;

    cin >> M >> N >> K;

    for(int i = 0 ; i  < K ;i++){
        int leftX, leftY, rightX, rightY;
        cin >> leftX >> leftY >> rightX >> rightY;

        for(int j = leftX ; j < rightX;j++){
            for(int k = leftY; k<rightY;k++){
                map[j][k]=1;
            }
        }
    }

    // 그래프 탐색
    for(int i = 0 ; i < N ;i++){
        for(int j = 0 ; j <M;j++){
            if(visited[i][j] == true || map[i][j]==1){
                continue;
            }
            queue<pair<int,int>> q;
            q.push({i,j});
            visited[i][j] = true;
            int width = 1;
            cnt++; // 시작 노드 개수 == 나눠진 영역 

            while(!q.empty()){
                int curX = q.front().first;
                int curY = q.front().second;
                q.pop();

                for(int dir = 0 ; dir<4 ;dir++){
                    int nx = curX + moveX[dir];
                    int ny = curY + moveY[dir];
                    // 범위
                    if(nx < 0 || nx >= N || ny < 0 || ny >= M ) continue;

                    // 이미 방문했거나 사각형이 막혀있을 경우
                    if(visited[nx][ny] == true || map[nx][ny]==1){
                        continue;
                    }

                    q.push({nx,ny});
                    visited[nx][ny]=1;
                    width++;
                }
                
            }
            ans.push_back(width);
        }
    }
    sort(ans.begin(),ans.end());
    cout << cnt<<'\n';
    for(int v:ans){
        cout << v << " ";
    }
    return 0;

}