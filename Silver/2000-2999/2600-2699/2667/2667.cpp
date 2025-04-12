#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<queue>
#include<string.h>
using namespace std;

const int dx[4] = {-1, 0 , 1 , 0};
const int dy[4] = {0, -1, 0, 1};
int map[26][26];
int visitied[26][26]={0,};
int N;
queue<pair<int,int>> q;
int groupCheck[626];

void bfs(int x, int y, int cnt){
    q.push({x,y});
    visitied[x][y]= cnt;
    while(!q.empty()){
        int curX = q.front().first;
        int curY = q.front().second;
        q.pop();
        for(int i = 0 ; i < 4;i++){
            int nextX = curX+dx[i];
            int nextY = curY+dy[i];
            if(nextX<0 ||nextY>=N||nextX<0 ||nextY>=N ) continue;
            if(visitied[nextX][nextY]==0 && map[nextX][nextY]==1){
                visitied[nextX][nextY] = cnt;
                q.push({nextX,nextY});
                
            }    
            
        }
    
    }
    return;
}


int main(){
    int cnt = 0;
    cin >> N;

    // // 배열 초기화 
    fill(&map[0][0], &map[26][26],0);

    for(int i = 0 ; i< N;i++){
        string a;
        cin >> a;
        for(int j = 0 ; j < N;j++){
            map[i][j] = a[j]-'0';

        }
    }

    for(int i = 0 ; i< N;i++){
        for(int j = 0 ; j < N;j++){
            if(visitied[i][j]==0){
                if(map[i][j]==1){
                    bfs(i,j,++cnt);
                }
            }


        }
    }

    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){ 		
            if(visitied[i][j]!=0){	
                groupCheck[visitied[i][j]]++;
            }
        }
    }

    sort(groupCheck+1, groupCheck+cnt+1);
    cout << cnt << endl;
    for(int i=1;i<=cnt;i++)
        cout << groupCheck[i] << endl; 
    return 0;

}