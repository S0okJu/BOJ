#include<iostream>
#include<string>
#include<stack>
using namespace std;

/*
8 진수 -> 2진수
314 = 11001100
3 = 11
1 = 001
4 = 100

8진수의 가장 오른쪽 수부터 3자리 2진수로 바꿔준다.
*/

string octal;
stack<int> binary;

void solution(){
    cin >> octal;
    if(octal == "0"){
        cout << 0 << endl;
        return;
    }

    int Os = octal.size();
    for(int i = Os-1; i>=0;i--){
        int cur = octal[i]-'0';
        for(int j = 0 ; j < 3;j++){
            int num = cur%2;
            cur /=2;
            binary.push(num);
        }
    }

    while(binary.top()!=1){
        binary.pop();
    }
    while(!binary.empty()){
        cout << binary.top();
        binary.pop();
    }
    cout << endl;
}
int main(){
    solution();
    return 0;
}