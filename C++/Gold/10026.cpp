#include<iostream>
#include<string>
#include<queue>
#include<algorithm>
using namespace std;

const int ran = 101;
const int dx[4] = {-1, 0, 1 ,0};
const int dy[4] = {0, 1, 0, -1};
int color[ran][ran];
int visited[ran][ran];
queue<pair<int,int>> q;
int cntBlindness;//적록 색맹인 경우
int cnt;// 적록 색맹이 아닌 경우
int N;
bool flag;

void bfs(int checkType){
    while(!q.empty()){
        int qs = q.size();
        while(qs--){
            int curX = q.front().first;
            int curY = q.front().second;
            int curColor = color[curX][curY];
            q.pop();
            for(int i = 0 ; i < 4; i++){
                int x = curX + dx[i];
                int y = curY + dy[i];
                int nextColor = color[x][y];

                if((x <0 || x >=N||y <0 || y >=N)||visited[x][y]) continue;
                if((flag && (nextColor=='R' ||nextColor=='G')) || curColor==nextColor ){
                    visited[x][y] = 1;
                    q.push({x,y});
                }
            }
        }
    }
    if(checkType ==0) cnt++;
    else cntBlindness++;

}


int main(){
    cin >> N;

    for(int i = 0 ; i < N ;i++){
        string a;
        cin >> a;
        for(int j = 0 ; j<N;j++){
            color[i][j] = a[j];
        }
    }

    for(int i=0;i<N;i++){
        for(int j = 0 ; j < N; j++){
            if(!visited[i][j]){
                q.push({i,j});
                bfs(0);
            }
        }
    }

    memset(visited, 0, sizeof(visited));

    for(int i = 0 ; i < N;i++){
        for(int j = 0 ; j < N ;j++){
            if(!visited[i][j]){
                if(color[i][j]=='R'|| color[i][j]=='G') flag = true;
                else flag = false;
                
                q.push({i,j});
                bfs(1);
            }
        }
    }
    cout << cnt << " "<<cntBlindness;
    return 0;
}