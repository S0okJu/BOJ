#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    double sum = 0;
    int MaxValue = -1; // 최대 최빈값 구하는 변수
    bool findSecond = false; // 최빈값이 같은 경우 확인 
    int FValue; // 최빈값 

    vector<int >freq(8001,0); // 최빈값을 구한느 벡터 
    vector<int> a;
    
    cin >> N;

    for(int i = 0 ; i < N; i++){
        int b;
        cin >> b;
        a.push_back(b);

        int temp = b <= 0 ? abs(b):b +4000; 
        freq[temp]++;

        MaxValue = max(MaxValue,freq[temp]);
        sum += b; // 산술 평균을 구하기 위한 합
        

    }
    
    sort(a.begin(),a.end()); 
    // 중앙값을 구하기 위한 값, 최빈값을 사용할때도 사용.

    
    for(int i = -4000;i<4001;i++){
        int temp = i<=0?abs(i):i+4000;
        if(freq[temp]==MaxValue){
            FValue = i;
            if(findSecond){
                break;
            }
            findSecond = true;
        }
    }

    cout << round(sum/(double)N)<<'\n'; // 산술 평균
    cout << a[N/2]<<'\n'; // 중앙값
    cout<< FValue<<'\n';
    cout<< a[N-1] - a[0]<< '\n'; // 범위 


    return 0;

}