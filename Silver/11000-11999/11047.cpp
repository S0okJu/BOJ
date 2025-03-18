#include<iostream>
using namespace std;

long long int money[10];
int main(){
    int M, K;
    int cnt = 0;
    cin >> M >> K;

    for(int i = 0 ; i < M ; i++){
        cin >> money[i];
    }
    for(int i = M-1; i>=0;i--){
        if(money[i]<=K){
            cnt+=(K/money[i]);
            K-=(money[i]*(K/money[i]));

            if(K==0)break;
        }
    }

    cout << cnt;
    return 0;

}