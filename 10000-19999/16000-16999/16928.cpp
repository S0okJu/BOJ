#include<iostream>
#include<vector>
#include<string.h>
#include<queue>
#include<algorithm>
using namespace std;

int snake, ladder;
vector<int> moveTo[101];
int visited[101];
queue<pair<int,int>> q;

int bfs(){
    int ans = 0x3f3f3f3f;
    q.push({1,0});
    visited[1] = 1;

    while(!q.empty()){
        int start = q.front().first;
        int throwNum = q.front().second;
        if(start == 100){
            ans = min(ans,throwNum);
            break;        
        }
        q.pop();

        for(int i = 1; i <=6; i++){
            int nx = start + i;
            if(nx >100 || visited[nx]){
                continue;
            }
            visited[nx]=1;
            if(!moveTo[nx].size()) q.push({nx,throwNum+1});
            else q.push({moveTo[nx][0],throwNum+1});
        }

    }
    return ans;
}
int main(){

    memset(visited,0,sizeof(visited));

    cin >> ladder>>snake;

    // 입력 받기
    for(int i = 0 ; i < ladder+snake;i++){
        int a, b;
        cin >> a >> b;
        moveTo[a].push_back(b);
    }

    int cnt = bfs();
    cout <<cnt;

    return 0;
}