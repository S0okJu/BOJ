# include<iostream>
#include<algorithm>
using namespace std;

int group[1001];
int main(){
    int N, M;
    int ans = (int)1e9;
    cin >> N >> M;
    
    for(int i = 0; i < M;i++){
        int x;
        cin >> x;
        group[x]=1;
    }

    for(int i = 1 ; i < 1001; i++){
        if(group[i]==1) continue;
        for(int j =i ; j< 1001;j++){
            if(group[j]==1) continue;
            for(int k = j; k <= 1001; k++){
                if(group[k]==1) continue;
                ans = min(ans, abs(N-(i*j*k)));
            }

        }
    }
    cout << ans;
    return 0;
}