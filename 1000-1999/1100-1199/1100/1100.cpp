#include<iostream>
#include<algorithm>
using namespace std;
char matrix[8][8];

int main(){
    int cnt = 0;
    for(int i = 0 ; i < 8 ;i++){
        for(int j = 0 ; j < 8;j++){
            cin >> matrix[i][j];
            if(i%2 ==0 && j%2 ==0 && matrix[i][j]=='F'){
                cnt++;
            }
            else if(i%2 == 1 && j%2 ==1&& matrix[i][j]=='F'){
                cnt++;
            }
        }
    }
    cout << cnt;
    return 0;
}