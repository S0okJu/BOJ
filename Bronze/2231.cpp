#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int N;
    int Value;
    int sum = 0;
    int cmpValue;
    
    cin >> N;
    cmpValue = 0; 

    while(true){
        // 0부터 1씩 더해 N의 생성자인지 확인한다. 

        sum = ++cmpValue;
        int Value = cmpValue; // 임의의 변수를 지정

        while(Value != 0){ // %연산자 이용해 각 자리의 숫자를 더함
            sum += (Value%10);
            Value/=10;
        }
        
        if(cmpValue == N ){ // cmpValue == N인 경우 생성자 생성 불가능 
            cout << "0";
            break;
        }
        if(N == sum){
            cout << cmpValue;
            break;
        }

        sum = 0;
    }

    return 0;
}