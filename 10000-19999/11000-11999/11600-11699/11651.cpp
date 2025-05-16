#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;

bool cmp(pair<int,int> a, pair<int,int> b){
    if(a.second != b.second)return a.second<b.second;
    else if(a.second == b.second) return a.first<b.first;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    vector<pair<int,int>> graph;
    vector<pair<int, int> >::iterator iter;

    int N;

    cin >> N;

    for(int i = 0 ; i < N;i++){
        int x, y;
        cin >> x >> y;
        graph.push_back(make_pair(x,y));
    }
    sort(graph.begin(),graph.end(),cmp);

    for(iter=graph.begin();iter!=graph.end();iter++){
        cout << iter->first <<" "<<iter->second<<'\n';
    }

    return 0;
}   