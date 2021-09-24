#include<iostream>
#include<string>

using namespace std;

int main(){
    string c;
    int max = 0;
    int count = 0;
    int target;
    int a[26] = {0,}; // alphabet

    cin >> c;


    for(int i = 0; i < c.length();i++){
        if(c[i] >= 'a' && c[i] <='z') c[i] -='a'-'A';
        a[c[i]-'A']++; // 해당 대문자의 값 count
    }

    for(int i = 0 ; i < 26 ;i++){
        if(max < a[i]){
            max = a[i];
            count = 0;
            target = i;// 가장 많은 개수를 가진 문자 
        }

        if(max==a[i]){
            count++;
        }
    }

    if(count > 1) cout << "?";
    else cout << (char)(target+'A');

    return 0;
    //소문자와 대문자의 아스키 코드 차이는 32이다.(그래서 'a'-'A'라고 표현)
}