#include<iostream>
#include<queue>
using namespace std;

int graph[101][101];

queue<int> q;

void bfs(int v){
    
}

int main(){
    int N; //정점 수

    fill(&graph[0][0], &graph[101][101],0);

    cin >> N;

    for(int i = 0 ; i < N;i++){
        for(int j = 0 ; j <N;j++){
            cin >> graph[i][j];
        }
    }
    
    for(int k = 0 ; k < N;k++){
        for(int i = 0 ; i < N;i++){
            for(int j = 0 ; j < N;j++){
                if(graph[i][k] && graph[k][j]){
                    graph[i][j]=1;
                }
            }
        }
    }

    for(int i = 0 ; i < N;i++){
        for(int j = 0 ; j <N;j++){
            cout << graph[i][j]<<" ";
        }
        cout <<"\n";
    }

}