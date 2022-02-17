#include<iostream>
#include<cmath>
using namespace std;

int func(int N,int a, int b){
    int ans = 0;
    while(a!=b){
        a = ceil(a/2);
        b = ceil(b/2);
        ans++;
    }
    if(ans == 0) return -1;
    return ans;
}
int main(){
    int N, A,B;
    cin >> N >> A >> B;
    int result = func(N,A,B);
    cout << result;
    return 0;
}