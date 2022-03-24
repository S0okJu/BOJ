#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int N[2];
    int arr[2][2];
    int sum = 0;
    cin >> N[0] >> N[1];

    for(int i = 0 ; i <2;i++){
               
        if(N[i]%4==0){
            arr[i][1] = (N[i]/4); 
            arr[i][0]= 4;
        }
       else{
            arr[i][1] = (N[i]/4)+1; 
            arr[i][0]= (N[i]%4);
       }
    }
    cout << abs(arr[1][0]-arr[0][0])+abs(arr[1][1]-arr[0][1]);


}