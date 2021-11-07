#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
using namespace std;

int main(){
    int N;
    vector<int> num;
    cin >> N;
    for(int i = 0 ;  i< N ;i++){
        int a;
        cin >> a;

        num.push_back(a);
    }

    sort(num.begin(),num.end());

    for(int i = 0 ; i < N ;i++){
        cout << num[i]<<'\n';
    }

    return 0;
}