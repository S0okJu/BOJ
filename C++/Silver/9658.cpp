#include<iostream>
using namespace std;
/*
 돌을 n개 빼냈을 때, 창영이가 모두 승리하는 상황이라면, 상근이는 패배하고, 
 반대로 창영이가 지는 상황이 단 하나라도 있으면, 상근이가 승리한다.
*/
int main(){
    int N;
    cin >> N;
    if(N%7==1 ||N%7==3)cout << "CY";
    else cout<<"SK";

    return 0;
}