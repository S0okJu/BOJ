#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>
using namespace std;

bool cmpFunc(pair<int,int> a, pair<int,int> b){
    if(a.second > b.second) return true;
    return false;
}

int main(){
    vector<pair<int,int>> time;
    int N;
    int value;
    cin >> N;

    for(int i = 0 ; i< N; i++){
        int T, S;
        cin >> T >> S;
        time.push_back({T,S});
    }

    sort(time.begin(),time.end(),cmpFunc);
    value = time[0].second - time[0].first;

    for(int i = 1; i < N;i++){
        if(value >time[i].second){
            value-=(value-time[i].second);
            cout<< i<<": "<<value<<'\n';
        }

        value -=time[i].first;
        
    }
    value =value>0 ?value:-1; 
    cout << value;
    return 0; 
}