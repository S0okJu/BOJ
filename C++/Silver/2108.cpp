#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
using namespace std;

int mean(vector<int> &a,int n){
    int sum = 0;
    for(int i = 0 ; i < n; i++){
        sum += a[i];
    }
    return round(sum / (double)n);
}

int med(vector<int> &a,int n){
    return a[n/2];
}

int freq(vector<int> &a,int n){
    map<int,int> mapping;
    int maxF = -1;
    vector<int> f;
    for(int i = 0 ; i <n ;i++){
        if (mapping[a[i]]) mapping[a[i]]++;
        else{
            mapping[a[i]] =1;
        }
    }

    for(auto p:mapping){
        if(maxF < p.second){
            maxF = p.second;
        }
    }

    for(auto p:mapping){
        if(maxF == p.second){
            f.push_back(p.first);
        }
    }
    sort(f.begin(),f.end());
    if(f.size()==1) return f[0];
    else return f[1];

}

int gap(vector<int> &a, int n){
    int minVal = 4000;
    int maxVal = -4000;
    if(a.size()>=2){
        for(int i = 0 ; i < n;i++){
            minVal = min(minVal,a[i]);
            maxVal = max(maxVal,a[i]);
        }
        return maxVal - minVal;
    }
    return 0;
    
}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    vector<int> a;
    
    cin >> N;

    for(int i = 0 ; i < N; i++){
        int b;
        cin >> b;
        a.push_back(b);

    }
    
    sort(a.begin(),a.end()); 
    // 중앙값을 구하기 위한 값, 최빈값을 사용할때도 사용.

    cout << mean(a,N)<<'\n'; // 산술 평균
    cout << a[N/2]<<'\n'; // 중앙값
    cout<< freq(a,N)<<'\n';
    cout<< gap(a,N)<< '\n'; // 범위 


    return 0;

}