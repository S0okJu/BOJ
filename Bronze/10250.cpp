#include<iostream>
using namespace std;

int main(){
    int T;
    int h, w, n;
    int i;

    cin >> T;

    for(i = 0 ; i < T;++i){
        cin >> h >> w >> n;

        if((n-1)/h+1 >= 10) cout << (n-1)%h+1 << (n-1)/h+1<<'\n';
        else cout<<(n-1)%h+1 <<0<<(n-1)/h+1<<'\n';
    }

    return 0;
}