#include<iostream>
#include<cmath>
using namespace std;

int func(int N,int a, int b){
    int ans = 0;
    while(a!=b){
        a = (a+1)/2;
        b = (b+1)/2;
        ans++;
    }
    return ans;
}
int main(){
    int N, A,B;
    cin >> N >> A >> B;
    int result = func(N,A,B);
    cout << result;
    return 0;
}