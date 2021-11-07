#include<iostream>
using namespace std;
// 2의 배수인 경우 창영이가 이기고, 2의 배수가 아닌 경우 상근이가 이긴다. -> 완벽한 게임이기 때문
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    long long int N;
    cin >> N;

    if(N%2 == 1){
        cout << "SK";
    }
    else{
        cout << "CY";
    }
    return 0;
}