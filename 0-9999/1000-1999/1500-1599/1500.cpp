#include<iostream>
using namespace std;

int main(){
    int s, k;
    long long ans = 1;
    cin >> s >> k;

    for(int i = 0 ; i < k;i++){
        if(i<(s%k)){
            ans = 1L * ans *((s/k)+1);
        }
        else{
            ans = 1L * ans *(s/k);
        }
    }
    cout << ans;
    return 0;
    
}