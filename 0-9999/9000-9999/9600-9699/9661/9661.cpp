#include<iostream>
using namespace std;

int main(){
    long long int N;
    cin>> N;

    // int arr[N];
    // arr[1] = arr[3] =arr[4]= 1;
    // for(int i = 5;i<=N;i++){
    //     if(!(arr[i-1]==1 &&arr[i-4]==1 )){
    //         arr[i] = 1;
    //     }
    // }
    // for(int i = 1; i<=N;i++){
    //     if(arr[i]==0){
    //         cout << i<<'\n';
    //     }
    // }
    
    if((N%5)==0 || (N%5)==2){
        cout << "CY";
    }
    else{
        cout << "SK";
    }
    return 0;
}