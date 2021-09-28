#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int N;
    int Value;
    int ind = 0;
    int sum = 0;
    int cmpValue;
    
    cin >> N;
    cmpValue = 0;

    while(true){

        sum = ++cmpValue;
        int Value = cmpValue;
        while(Value != 0){
            sum += (Value%10);
            Value/=10;
        }
        
        if(cmpValue == N ){
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