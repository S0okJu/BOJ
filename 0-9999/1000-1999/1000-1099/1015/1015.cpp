#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

vector<pair<int,int>> num;
int b[1001];
int main(){
    int N;
    int cnt = 0;
    cin >> N;

    for(int i = 0 ; i < N;i++){
        int a;
        cin >> a;
        num.push_back({a,i});
    }

    sort(num.begin(),num.end());
    for(int i = 0 ; i<N;i++){
        b[num[i].second]= i;
    }
    for(int i= 0 ; i < N;i++){
        cout << b[i]<<" ";
    }
    return 0;

}