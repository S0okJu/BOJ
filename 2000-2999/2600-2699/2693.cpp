#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;
    cin >> T;

    for(int i = 0 ; i < T ;i++){
        vector<int> a;
        for(int j = 0 ; j<10;j++){
            int v;
            cin >> v;
            a.push_back(v);
        }
        sort(a.begin(),a.end(),greater<int>());
        cout<<a[2]<<'\n';
    }

    return 0;
}