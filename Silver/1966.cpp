#include<iostream>
#include<algorithm>
#include<queue>
#include<utility>
using namespace std;

int main(){
    int T;
    
    cin >> T;

    for(int i = 0 ; i < T; i++){
        int N, M;
        int cnt = 0;
        queue<pair<int,int>> q;
        priority_queue<int> priorityQ;
        cin >> N >> M;

        for(int j = 0 ; j < N; j++){
            int a;
            cin >> a;
            priorityQ.push(a);
            if(j == M){
                q.push(make_pair(a,1));
            }
            else q.push(make_pair(a,0));
        }
        


        while(!q.empty()){
            int CurrentFirst = q.front().first;
            int CurrentSecond = q.front().second;

            q.pop();
            if(CurrentFirst == priorityQ.top()){
                cnt++;
                if(CurrentSecond==1){
                    cout<<cnt<<'\n';
                    break;
                }
                priorityQ.pop();

            }
            else{
                q.push(make_pair(CurrentFirst,CurrentSecond));
            }
        }   
    }


    return 0;
}
