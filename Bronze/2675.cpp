#include<iostream>
#include<string>
using namespace std;

int main(){
    int T;
    int repNum = 0;
    string ans = "";
    string* str;

    cin >> T;
    str = new string[T];

    for(int i = 0 ; i<T;i++){
        cin >> repNum >>str[i];

        for(int j = 0; j < str[i].length();j++){
            ans.append(repNum,str[i][j]);
        }
        cout << ans<<endl;
        ans ="";
        repNum = 0;
    }
    delete[] str;
}