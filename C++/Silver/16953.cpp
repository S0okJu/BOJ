#include<iostream>
#include<queue>
#include<cmath>
#include<algorithm>
using namespace std;

int A, B;
queue<pair<long long int, int>> q;


int main(){
    cin >> A >> B;
    q.push({A,0});
    while(!q.empty()){
        int value = q.front().first;
        int cnt = q.front().second;
        q.pop();
        if(2*value <= B){
            q.push({2*value,cnt+1});
        }
        if(value*10 +1 <= B){
            q.push({value*10 + 1,cnt+1});
        }
        if(value == B){
            cout << cnt + 1;
            return 0;
        }
    }
    cout << -1;
    return 0;
}