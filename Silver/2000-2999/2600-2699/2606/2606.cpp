#include <iostream>
#include <vector>
#include <stack>
using namespace std;

bool visitied[101];
vector<int> v[101];
int cnt = 0;

void dfs(int n){
    if(!visitied[n]){
        cnt++;
        visitied[n]=true; // 방문했다고 표시하기
    }

    for(int i = 0 ; i <v[n].size();i++){
        if(visitied[v[n][i]])continue;// 만약 방문을 했다면
        else dfs(v[n][i]); // 방문을 하지않았다면  탐색하기 
    }   
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int computer;
    int computerConnection;
    cin >> computer;
    cin>>computerConnection;
    
    for(int i = 0 ; i<computerConnection;i++){
        int v1, v2;
        cin >> v1 >> v2;
        v[v1].push_back(v2);
        v[v2].push_back(v1);
    }
    visitied[1] = true; // 1이후부터 카운트를 해야하므로 방문했다고 표시해야한다. 
    dfs(1);
    cout << cnt;
    return 0;
}