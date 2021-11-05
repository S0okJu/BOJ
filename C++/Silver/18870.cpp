#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;

bool func(pair<int,int> a, pair<int,int> b){
    if(a.second <= b.second){
        return a.second < b.second;
    }
    return a.second < b.second;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    vector<pair<int,int>> point;
    
    int T;
    cin >> T;
    int *value = new int[T];
    for(int i = 0 ; i< T; i++){
        int a;
        cin >> a;
        point.push_back(make_pair(a,i));
    }

    sort(point.begin(),point.end());

    int check = 0;
    for(int i = 0 ; i< T ; i++){
        value[i] = point[i].first;
        if(i>0){
            if(value[i-1] != point[i].first){
                check++;
            }
         
        }     
        point[i].first = check;
    }

    sort(point.begin(),point.end(),func);

    for(int i = 0 ; i< T;i++){
        cout << point[i].first<<" ";
    }
    delete[] value;
    return 0;
}