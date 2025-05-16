#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int N, K;
    // 범위를 고려해 int 대신 long long을 사용한다. 
    long long maxNum=0; 
    long long cnt = 0;
    long long start = 1;
    long long end = 0, mid = 0;
    long long* num;
    long long ans;

    cin >> N >> K;

    num = new long long[N];
    for(int i = 0 ; i< N; i++){
        cin >> num[i];
        maxNum = max(maxNum,num[i]); // 값의 범위를 알기 위해 최댓값을 구한다.
    }
    // *** 정렬을 해서 마지막 인덱스를 구하는 방법도 있다. 

    end = maxNum;

    // 이분 탐색 시작 
    while(start<=end){
        cnt = 0;
        mid = (start+end)/2;

        for(int i = 0 ; i < N ;i++){
            cnt +=(num[i]/mid);
        }

        
        if(cnt >= K ){ 
            // 문제에서 N개의 랜선보다 많이 만들어도 N개라고 한다. 라는 문장이 있다. 
            // 최대값을 구하는 문제이므로 break를 사용하지 않고 끝까지 이분 탐색을 실행한다. 
            start = mid+1;
            ans = mid;
        } 
        else  end = mid-1;
    }

    cout << ans;

    delete[] num;
    return 0;
}

