#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

int N, M, R;
vector<bool> visit(100001,false);
int dist[100001];
int u, v;

vector<int> mapping[100001];
queue<int> q;
int cnt = 1;

void bfs(int v){
    q.push(v);
    visit[v]=true;
    while(!q.empty()){

        int cur= q.front();
        q.pop();
        dist[cur] = cnt++;
        for(vector<int>::size_type i = 0 ; i < mapping[cur].size() ;i++){
            int next = mapping[cur][i];
            if(visit[next]==false ){
                visit[next]=true;
                q.push(next);
            }
        }
    }
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M >> R;

    for(int i = 0 ; i< M; i++){
        cin >> u >> v;
        mapping[u].push_back(v);
        mapping[v].push_back(u);
    }
    for(int i=1; i<=N; i++){
		sort(mapping[i].begin(), mapping[i].end());
	}

    bfs(R);

    for(int i = 1 ; i <=N;i++ ){
        cout <<(dist[i]==0?0:dist[i])<<'\n';
    }
    return 0;
}