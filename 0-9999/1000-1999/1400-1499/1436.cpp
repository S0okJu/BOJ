#include<iostream>
using namespace std;

int main(){
    int N;
    int value = 0;
    int tmpValue = 0;
    int checkFlag = 0;
    int count = 0;
    
    cin >> N;

    while(++value){
        tmpValue = value; // 세상의 종말인지 확인하기 위해서는 조작이 필요하므로 tmp을 만든다.
        checkFlag = 0; //모든 값의 checkFlag를 확인하므로 초기화해야한다. 

        while(tmpValue){
            if(tmpValue%1000 ==666){// 세상의 종말이라면
                checkFlag = 1;
                break;
            }
            tmpValue/=10; //더 자세하게 세상의 종말인지 체크 

        }

        if(checkFlag==1){
            count++;
            if(count == N){
                cout << value;
                break;
            }
        }
    }

    return 0;

}