#include<iostream>
#include<queue>
#include<algorithm>
using namespace std;

int N, M, H;
int a[101][101][101];
int dx[] = {-1, 0, 1, -1, 0, 0};
int dy[] = {0, 1, 0, -1, 0 ,0};
int dz[] = {0, 0,0, 0, -1, 1};
queue<pair<int,pair<int,int>>> box;

void bfs(){

    while(!box.empty()){

        int x = box.front().first;
        int y = box.front().second.first;
        int z = box.front().second.second;
        box.pop();

        for(int i = 0 ; i < 6; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            int nz = x + dz[i];

            if(nx < 0 || nx >= M || ny <0 || ny >= N|| nz <0 || nz >= H)continue;
            if(a[nx][ny][nz])continue;

            a[nx][ny][nz] = a[x][y][z]+1;
            box.push({nx,{ny,nz}});
        }
    }
}
int main(){
    int ans = 0;
    cin >> M >> N >> H;

    for(int i = 0 ; i < H;i++){
        for(int j = 0 ; j< N;j++){
            for(int k = 0 ; k < M;k++){
                cin >> a[i][j][k];
            }
        }
    }

    bfs();
    for(int i = 0 ; i < H;i++){
        for(int j = 0 ; j< N;j++){
            for(int k = 0 ; k < M;k++){
                if(a[i][j][k]==0){
                    cout << "-1";
                    return 0;
                }
                if(ans < a[i][j][k]) ans = a[i][j][k];
            }
        }
    }
    cout<< ans-1<<'\n';
    return 0;

}