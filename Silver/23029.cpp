#include<iostream>
#include<algorithm>
using namespace std;

int food[100001];
int DP[100001];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    int N;
    int Zero = 0;
    cin >> N;
    int secondZero = 0;

    for(int i = 1 ; i <= N ;i++){
        cin >> food[i];
    }
    if(food[1]==0) Zero = food[2];
    else Zero = food[2]/2;

    DP[1] = food[1];
    DP[2] = food[1]+Zero;
    for(int i = 3; i <=N;i++){
        if(food[i-1]==0) secondZero = food[i];
        else secondZero = food[i]/2;
        DP[i] = max(DP[i-3]+food[i-1]+secondZero,DP[i-2]+food[i]);
        DP[i] = max(DP[i],DP[i-1]);

    }

    cout << DP[N];

    return 0;    
}