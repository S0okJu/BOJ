#include<iostream>
#include<cstring>
#include<string>
using namespace std;

int main(){
    bool f = 0;
    int t, visit1[26], visit2[26], ans = 0;
    string str[101];

    cin >> t;
    
    for(int i = 0 ; i < t; i++){
        cin >> str[i];
    }


    for(int i = 0 ; i < t-1;i++){
        for(int j = i+1;j<t;j++){
            if(str[i].length()!=str[j].length()) continue;

            f= 0;
            memset(visit1, -1, sizeof(visit1));
            memset(visit2, -1, sizeof(visit2));

            for (int k = 0, len = str[i].length(); k < len; ++k) {
                if (visit1[str[i][k] - 'a'] != -1 && visit1[str[i][k] - 'a'] != str[j][k] - 'a') {
                    f = 1;
                    break;
                }
                if (visit2[str[j][k] - 'a'] != -1 && visit2[str[j][k] - 'a'] != str[i][k] - 'a') {
                    f = 1;
                    break;
                }
                visit1[str[i][k] - 'a'] = str[j][k] - 'a';
                visit2[str[j][k] - 'a'] = str[i][k] - 'a';
                cout << str[i][k]<<' '<<visit2[str[j][k]]<<'\n';
            }
            if (f) continue;
            ans++;

        }
    }
    cout << ans;
    return 0;
}