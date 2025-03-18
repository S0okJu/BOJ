#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;

int main(){
    int N;
    vector<pair<int,int>> meeting;
    
    cin>> N;
    for(int i = 0 ;  i < N ;i++){
        int a, b;
        cin >> a >> b;
        meeting.push_back({b,a});
    }
    sort(meeting.begin(),meeting.end());

    int cnt = 1;
    int lastTime = meeting[0].first;

    for(int i = 1 ; i < meeting.size();i++){
        int nextTime = meeting[i].second;
        if(lastTime > nextTime) continue;
        lastTime = meeting[i].first;
        cnt++;
    }

    cout <<cnt;
    return 0;
}