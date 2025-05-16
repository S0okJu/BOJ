#include<iostream>
using namespace std;

int a[64][64];

void func(int y, int x,int count){
    int cmpValue = a[y][x]; 

    for(int i = 0 ; i < count ;i++){
        for(int j = 0 ; j < count ;j++){
            if(a[y+i][x + j]!=cmpValue){
                cout << "(";
                func(y,x,count/2);
                func(y,x+count/2,count/2);
                func(y+count/2,x,count/2);
                func(y+count/2,x+count/2,count/2);
                cout << ")";
                return;
            }

        }
        
    }
    cout << cmpValue;
}

int main(){
    int N;
    cin >> N;

    for(int i = 0 ; i < N;i++){
        string input;
        cin >> input;

        for(int j = 0 ; j < input.length();j++){
            a[i][j] = input[j]-'0';
        }
    }
    func(0,0,N);
    return 0;

}