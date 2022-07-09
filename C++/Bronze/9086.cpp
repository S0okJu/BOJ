#include<iostream>
#include<string>
using namespace std;

int main(){
    int num;
    cin >> num;

    for(int i = 0; i < num; i++)
    {
        string s;
        string ans="";
        int strLen = 0;

        cin >> s;
        strLen = s.length();
        ans+=(s.substr(0,1)+s.substr(strLen-1,1));
        cout << ans<<'\n';
    }
    return 0;
}