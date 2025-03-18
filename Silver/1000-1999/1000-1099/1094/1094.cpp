#include<iostream>
using namespace std;

int main(){
    int X;
    int cnt = 0;
    cin >> X;
    int stick = 64;

    while(X>0){
        if(stick > X){ 
            stick /=2; // 절반으로 자르고(64 -> 32, 32), 하나를 버린다.
        }
        else{
            cnt++;
            X -= stick; 
        }
    }
    cout << cnt;
    return 0;
}