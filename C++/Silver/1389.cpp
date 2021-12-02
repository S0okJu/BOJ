#include<iostream>
#include<queue>
#include<vector>
#include<cstring>
using namespace std;

int N, M;
const int v_size = 5001;
int dist[v_size];
int cnt = 0;

vector<int>graph[v_size];
queue<int> q;


int bfs(int v){
    memset(dist, 0, sizeof(dist)); // 초기화 필수
    int cnt= 0 ;
    int cur = v;
    q.push(v);

    while(!q.empty()){
        int now = q.front();
        q.pop();
        cnt += dist[now];

        for(int next:graph[now]){
            if (dist[next]) continue;
            dist[next] = dist[now]+1;
            q.push(next);
        }
    }
    return cnt;
}
int main(){
    cin >> N >> M;

    for(int i = 0 ; i < M ;i++){
        int a, b;
        cin >> a >> b;

        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    int mcnt = 1e9;
    int midx = 1;

    for(int i = 1; i <=N;i++){
        int countR = bfs(i);
        if(countR < mcnt){
            mcnt = countR;
            midx = i;
        }
    }
    cout << midx;
    return 0;
}