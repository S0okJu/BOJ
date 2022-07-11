#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int main(){
    string inp;
    int ans = 0;
    cin >> inp;

    for(int i=0 ; i< inp.length();i++)    
    {
        ans +=pow(inp[i]-'0',5);
    }
    cout << ans;
    return 0;
}