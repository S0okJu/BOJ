#include<iostream>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int i = 0 ; i < T;i++){
        int a, b;
        int remainder = 1;
        cin >> a >> b;
        for(int j = 0 ; j < b;j++){
            remainder = (remainder * a)%10;
        }
        if(remainder==0){
            cout << 10;
        }
        else{
            cout << remainder;
        }
        cout << "\n";
    }
}