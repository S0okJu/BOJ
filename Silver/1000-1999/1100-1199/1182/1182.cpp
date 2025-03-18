#include<iostream>
#include<vector>
using namespace std;

int n, s;
int ans = 0;
int num[20];

void solve(int index, int sums){
    if(index >=n){
        if(sums == s){
            ans++;
        }
        return;
    }

    solve(index+1,sums+num[index]); // 원소를 포함하는 경우
    solve(index+1, sums); // 원소를 포함하지 않는 경우 

}
int main(){

    cin >> n >> s;

    for(int i = 0 ; i < n ;i++){
        cin >> num[i];
    }
    solve(0,0);
    if(s==0) ans--;
    cout << ans;
    return 0;

}