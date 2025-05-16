#include<iostream>
using namespace std;


int main(){
    int T;
    int N, M;

    cin >> T;

    for(int i = 0 ; i < T; i++){
        long long value = 1;
        cin >> N >> M;

        for(int i = 1 ; i <= N;i++){
            value = value *(M-i+1)/i; // 값을 곱할때 마다 i로 나눠준다.(범위 초과 방지)
        }
        cout << value <<endl;
    }

    return 0;
}
