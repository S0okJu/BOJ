#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main(){
    int T;
    cin >> T;

    while(T--){
        string a, ans;
        int cnt = 0;

        cin >> a;
        do{
            ans = a;
            if(++cnt == 2)break;
        }while(next_permutation(a.begin(),a.end()));
        cout << ans<<'\n';

    }
}