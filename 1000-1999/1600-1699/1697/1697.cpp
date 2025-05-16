#include<iostream>
#include<algorithm>
#include<queue>
using namespace std;

int N,K;
int dis[100002];

int main(){
    queue<int> Q;
    cin >> N >> K;

    fill(dis,dis+100001, -1);
    dis[N] = 0;
    Q.push(N);

    while(dis[K]==-1){
        int current = Q.front();
        Q.pop();

        for(int next :{current-1, current+1, 2*current}){
            if(next < 0 || next > 100000) continue;
            if(dis[next]!= -1)continue;
            dis[next] = dis[current]+1;
            Q.push(next);
        }
    }

    cout << dis[K];
    return 0;
}
