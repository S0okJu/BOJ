#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    int N; // 약수의 개수
    int value;
    int ans;
    vector<int> num;

    cin >> N;

    for(int i = 0 ; i < N;i++){
        cin >> value;
        num.push_back(value);
    }
    sort(num.begin(),num.end());

    ans = num[0] * num[N-1];
    cout << ans;

    return 0;

}