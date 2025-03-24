#include<iostream>
#include<vector>
using namespace std;

int N, M;
bool check[1001];
vector<int> graph[1001];

void dfs(int now){
    check[now] = true;
    for(int i = 0 ; i < (int)graph[now].size();i++){
        int next = graph[now][i];
        if(!check[next]){
            dfs(next);
        }
    }
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int count = 0;
    cin >> N >> M;
    
    for(int i = 0 ; i < M;i++){
        int u, v;
        cin >> u >> v;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for(int i = 1; i<=N;i++){
        if(!check[i]){
            dfs(i);
            count++;
        }
    }
    cout<< count;
    return 0;
}