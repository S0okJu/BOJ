#include<iostream>
using namespace std;

int arr[9][9];

int main(){
    int maxNum = -1;
    int maxI, maxJ;

    for(int i = 0 ; i < 9;i++){
        for(int j = 0 ; j < 9;j++){
            cin >> arr[i][j];
            if(arr[i][j]>maxNum){
                maxI = i+1;
                maxJ = j+1;
                maxNum = arr[i][j];
            }
        }
    }

    cout << maxNum<<"\n"<<maxI<<" "<<maxJ;
    return 0;
}