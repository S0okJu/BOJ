#include<iostream>
#include<map>
using namespace std;
int arr[11];
int ans[11];
int main(){

    int N;
    cin >> N;
    for(int i = 0 ; i < N;i++){
        cin >> arr[i];
    }

    for(int i = 0; i < N;i++){
        int cnt = 0;
        for(int j = 0 ; j < N;j++){
            if(arr[i]==cnt){
                if(!ans[j]){ans[j]=i+1; break;}
            }
            else{
                if(!ans[j]) cnt++;
            }
        }
    }

    for(int i = 0 ; i < N;i++){
        cout << ans[i]<<" ";
    }
    return 0;
}