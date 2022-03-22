#include<iostream>
using namespace std;

int arr[101][101];
int main(){
    int N, M;
    int ans=0;
    cin >> N >> M;
    
    for(int i = 0 ; i < N;i++){
        int x1,y1,x2,y2;
        cin >> x1 >> y1 >> x2>> y2;
        
        for(int xp = x1; xp <=x2;xp++){
            for(int yp=y1;yp<=y2;yp++){
                arr[xp][yp]+=1;
            }
        }
    }

    for(int i = 1 ; i<=100;i++){
        for(int j = 1 ; j <= 100;j++){
            if(arr[i][j]>M){
                ans++;
            }
        }
    }
    cout << ans;
    return 0;
}