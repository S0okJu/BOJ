#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int A, B, ans,remainder,powNum=1;
    int N;
    cin >> A >> B >> N;

    for(int i = 0 ; i < N; i++){
        remainder = A % B;
        remainder *=10;
        ans = remainder/B;
        A = remainder%B;
    }
    
    cout << ans;
    return 0;
}   