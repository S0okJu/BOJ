#include<iostream>
using namespace std;

int main(){
    int A, B, C;
    int cnt = 0;

    cin >> A >> B >> C;

    if((B-A-1) > (C-B-1)){
        cnt = B-A-1;
    }
    else{
        cnt = C-B-1;
    }
    cout << cnt;
    return 0;

}