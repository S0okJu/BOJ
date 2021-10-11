#include<iostream>
#include<string>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string L, R;
    long long count = 0;

    cin >> L >> R;
    //1. 자릿수가 다르다면 반드시 8이 포함되지 않는 숫자가 존재한다.
    if(L.length()!=R.length()){
        count = 0; 
    }
    else{ // 2. 자릿수가 같은 경우 8을 센다.
        for(int check = 0 ; check < L.length();check++){
            if(L[check]== '8' && L[check]==R[check]){
                count++;
            }
            else if(L[check]!=R[check]){ // 같은 자리에 숫자가 다른 경우 반드시 8이 존재하지 않는 숫자가 존재한다. 
                break;
            }
        }
    }
    cout << count;

    return 0;
}