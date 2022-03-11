#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
using namespace std;

struct Mapping{
    int len;
    string str;
};

bool cmp(Mapping &a, Mapping &b){
    return a.len > b.len;
}
int main(){
    Mapping word[50];
    int n, i, j, cnt = 0;
    
    cin >> n;

    for(int i = 0 ; i < n;i++){
        string a;
        cin >> a;
        word[i].len = a.length();
        word[i].str = a;
    }

    sort(word, word+n,cmp);

    for(int i =1 ; i< n;i++){
        for(int j = 0 ; j < i;j++){
            if(word[j].len && word[j].str.compare(0, word[i].len,word[i].str)==0){
                cnt++;
                word[i].len = 0;
                break;
            }
        }
    }
    cout << n-cnt;
    return 0;
}