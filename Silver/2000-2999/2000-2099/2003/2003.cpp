#include<iostream>
#include<vector>
using namespace std;

int main(){
    int N;
    long long int M;
    int sum = 0;
    int ans = 0;
    int first = 0,second = 0;
 
    cin >> N >> M;
    int *num = new int[N];

    for(int i = 0 ; i < N;i++){
        cin >> num[i];
    }
    while(true){
        if(sum < M){
            if(second==N)break;
            sum += num[second];
            second++;
            
        }
        else{
            sum-=num[first];
            first++;
        }
        if(sum==M){
            ans++;
        }
    }

    cout << ans;
    delete[] num;
    return 0;
}