#include<iostream>
#include<algorithm>
using namespace std;

void printArr(int a[]){
    for(int i = 0 ; i< 5 ;i++){
        cout << a[i]<<" ";
    }
    cout << "\n";
}
void swap(int& a, int& b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}
int main(){
    int arr[5];
    fill(&arr[0],&arr[5],0);

    for(int i = 0 ; i < 5;i++){
        cin >> arr[i];
    }

    for(int i = 0 ; i < 4;i++){
        for(int j =0 ; j < 4;j++){
            if(arr[j]>arr[j+1]){
                swap(arr[j],arr[j+1]);
                printArr(arr);
            }
        }
    }
    return 0;
}