#include<iostream>
using namespace std;


int main(){
    int cage[100000]={1,3};
    int N;

    cin >> N;
    for(int i = 2; i<=N;i++){
        cage[i]= (cage[i-1]*2+cage[i-2])%9901;
    }
    cout << cage[N];
    return 0;
}