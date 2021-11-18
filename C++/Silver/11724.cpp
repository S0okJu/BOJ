#include<iostream>
#include<vector>
using namespace std;

    
int N, M;
vector<int> graph[1001];

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N >> M;
    int first = 0;
    
    for(int i = 0 ; i < M;i++){

        int u, v;
        cin >> u >> v;
        if(i==0){
            first = u;
        }
        graph[u].push_back(v);
        graph[v].push_back(u);
        

    }
    cout << graph[first].size();
    return 0;
}