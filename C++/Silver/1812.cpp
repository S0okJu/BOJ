#include<iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    int arr[1000];
    int sum = 0;

    for(int i = 0; i < N;i++){
        cin >> arr[i];
        sum += arr[i];
    }
    sum /=2;

    for(int i = 0 ; i < N;i++){
        int tmp = 0;
        for(int j = 0 ; j < N; j+=2){
            tmp +=arr[(i+j)%N];
        }
        cout << tmp - sum <<'\n';
    }

    return 0;

}