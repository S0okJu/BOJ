#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int min(int a, int b){
    return a < b? a:b;
}
int main(){
    int N;
    int count = 0;
    int index = 1;
    long long cmpValue = 100000001;
    vector<long long> correctArr;


    cin >> N;
    
    for(int i = 0 ; i < N;i++){
        int a;
        cin >> a;
        correctArr.push_back(a);
    }
    sort(correctArr.begin(), correctArr.end());

    for(int i = 0 ; i < correctArr.size();i++){
        count =0; // 새롭게 다시 비교하므로 count 초기화 
        
        // 올바른 배열의 sample 배열 생성
        vector<long long> sample(5);
        for(int j = 0; j < 5; j++){
            sample[j] = correctArr[i]+j;
        }

        int k = i;
        //correctArr와 그 인덱스와 해당되는 sample 값을 하나하나씩 비교
        for(int cmp = 0 ; cmp < 5; cmp++){
            if(correctArr[k]==sample[cmp]&& k < correctArr.size()){
                k++;
                count++;
            }
        }
        // 최소값 
        cmpValue = min(cmpValue, 5-count);
    }

    cout << cmpValue;
    return 0;
}