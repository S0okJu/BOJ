#include<iostream>
#include<string>
using namespace std;

int main(){
    int N;
    int long_cnt;
    string ans ="";

    cin >> N;
    long_cnt = N/4;
    
    for(int i = 0 ; i < long_cnt;i++){
        ans+="long ";
    }
    ans+="int";
    cout << ans;

    return 0;
}