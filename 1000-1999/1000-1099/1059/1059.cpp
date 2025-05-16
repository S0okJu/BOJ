#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main(){
    int L, n;
    int sum = 0;
    int first = 0;
    int second = 1000;

    vector<int> group;

    cin >> L;
    for(int i = 0 ; i < L;i++){
        int a;
        cin >> a;
        group.push_back(a);
    }
    cin>> n;

    sort(group.begin(),group.end()); // 정렬

    for(int i = 0 ; i < L;i++){
        if(group[i]==n){
            cout<<0;
            return 0;
        }
        else if(group[i] > n){
            first = group[i-1]+1;
            if(i!=0){
                second = group[i]-1;
            }
            else{
                first =1;
                second = group[0]-1;
            }
            break;
        }
    }// 초기화

    
    while(first <= n){
        sum+=(second-first)-(n-1-first);// first, second 범위 차 - first에서 n-1까지 범위 (해당 안되는 부분)
        first++;
    }

    cout << sum-1; // first =n인 경우 1이 더 카운팅되므로 -1을 해준다.
    return 0;

}