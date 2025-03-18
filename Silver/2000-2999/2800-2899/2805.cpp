#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int N;
    long long M;
    int* arr;
    long long int findMax = 0;
    long long int ans = 0;
    long long int front = 0, mid = 0, end = 0;

    cin >> N >> M;

    arr = new int [N];
    for(int i = 0 ; i < N; i++){
        cin >> arr[i];
        findMax = arr[i] > findMax ? arr[i]:findMax;
    }

    front = 1;
    end = findMax;

    while(front <= end){
        long long int remainValue = 0;
        mid = (front+end)/2;

        for(int i = 0 ; i < N ;i++ ){
            if (mid < arr[i]) remainValue +=(arr[i]-mid);
        }

        if(remainValue < M) end = mid -1;
        else{
            front = mid + 1;
            if (mid > ans){
                ans = mid;
            } // 최댓값을 구하는 문제이므로 
        }
   
    }
    cout << ans;


    delete[] arr;
    return 0;
}