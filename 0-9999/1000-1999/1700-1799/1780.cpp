#include<iostream>
#include<cmath>
#include<string.h>
using namespace std;
int check[3];
int paper[2188][2188];
int N;

void func(int a, int b,int cur){
    int first = paper[a][b];
    bool checkFlag = true;

    for(int i = a ;  i< a+cur;i++){
        for(int j = b; j<b+cur;j++){
            if(first != paper[i][j]){
                checkFlag = false;
                break;
            }
        }
        if(checkFlag==false)break;
    }
    if(checkFlag == true){
        check[first+1]++;
        return;
    }
    int k = cur/3;
    for(int i = 0 ; i < 3;i++){
        for(int j = 0 ; j < 3;j++){
            func(a+i*k,b+j*k,k);
        }
    }

}


int main(){
    int divNum;
    cin >> N;

    divNum = cbrt(N);
    memset(check,0,sizeof(check));

    for(int i = 0 ; i<N;i++){
        for(int j =0;j<N;j++){
            cin >> paper[i][j];
        }
    }

    func(0,0,N);
    cout << check[0] << '\n'<<check[1]<<'\n'<<check[2];
    return 0;
}