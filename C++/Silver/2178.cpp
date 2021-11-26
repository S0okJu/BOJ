#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;

int N, M;
int cnt;
int maze[101][101];
int visited[101][101];
queue<pair<int,int>> s;
const int dx[] = {-1, 0 , 1, 0};
const int dy[] = {0, -1, 0, 1};


void bfs(int a, int b){

    while(!s.empty()){
        int x = s.front().first;
        int y = s.front().second;
        s.pop();

        for(int i = 0 ; i < 4 ; i++){
            int nx = x+dx[i];
            int ny =y + dy[i];

            if(nx < 0 || nx >= N || ny < 0 ||ny>=M){
                continue;
            }
            if(visited[nx][ny]>=0 || maze[nx][ny]!=1) continue;
            visited[nx][ny] = visited[x][y]+1;
            s.push({nx,ny});
        }
    }

}
int main(){

    cin >> N >> M;
    fill(&visited[0][0], &visited[N][M], -1);
    for(int i = 0 ; i < N ;i++){
        string input;
        cin >> input;
        for(int j = 0; j < input.length() ;j++){
            maze[i][j] = input[j]-'0';
        }
    }

    visited[0][0] = 0;
    s.push({0,0});
    bfs(0,0);
    cout << visited[N-1][M-1]+1;
    return 0;
}