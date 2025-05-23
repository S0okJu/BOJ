#include<iostream>
using namespace std;

int main(){
    int A, B;
    int idx = 0; // 인덱스
    int value = 1;// 값  
    int sum = 0;
    int num = 1; // 무슨 숫자 수열인지 
    int countNum = 0;// 수열의 개수
    cin >> A >> B;

    while(true){

        idx++;
        countNum++;

        if(idx > B) break;
        if(idx >= A && idx <=B){// A,B 범위 안에 있다면 더한다. 
            sum+=value;
        }

        if(countNum == num){
            num++;
            value++; // 수열의 숫자를 더해서 바꿔준다. . 
            countNum = 0; // 초기화 
        } 

    }

    cout << sum;
    return 0;
}
