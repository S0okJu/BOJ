#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

bool cmp(pair<int,int> a, pair<int,int> b){
    if(a.second>b.second){
        return a > b;
    }
    return a < b;
}
int main(){

    vector<pair<int,int>> input;

    int ans[3];
    int sum = 0;
    
    for(int i = 0 ; i<8;i++){
        int a;
        cin >> a;
        input.push_back({a,i});
    }
    sort(input.begin(),input.end(),greater<>());
    
    input.pop_back();
    input.pop_back();
    input.pop_back();

    sort(input.begin(),input.end(),cmp);
    for(int i = 0 ; i<5 ;i++){
        sum+=input[i].first;
    }

    cout << sum<<"\n";
    for(int i = 0 ; i<5 ;i++){
        cout << input[i].second+1<<" ";
    }
    return 0;
}

