#include<iostream>
using namespace std;
int a, b, c; 
int calc(int n, int k){
    if(k==0) return 1;

    int temp = calc(n,k/2);

    int result = (1LL * temp *temp) %c;

    if(k%2) result = (1LL * result * n)%c;
    return result;
}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> a >> b >> c;
    cout << calc(a,b);

    return 0;
}