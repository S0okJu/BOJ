#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

bool desc(int a, int b){ 
  return a > b; 
} 
int main(){
    int N;
    int inputValue;
    vector<int> A;
    vector<int> B;
    int sum = 0;
    cin >> N;
    
    for(int i = 0 ; i < N; i++){
        cin >> inputValue;
        A.push_back(inputValue);
    }

    for(int i = 0 ; i < N ; i++){
        cin >> inputValue;
        B.push_back(inputValue);
    }

    // 오름차순 정렬
    sort(A.begin(),A.end());


    // 내림차순 정렬
    sort(B.begin(),B.end(),desc);

    for(int i = 0 ; i < N ; i++){
        sum += A[i] * B[i];
    }

    cout << sum;
    return 0;
    
}