#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int n;
    int box[1001];
    cin >> n;
    int cnt = 0;

    for(int i = 0 ; i < n;i++){
        cin >> box[i];
    }

    int idx = 0;
    for(int i = 1 ; i <=1000;i++){
        for(int j = idx ; j <n;j++){
            if(box[j]==i){
                // cout << idx<<" "<<box[j]<<"\n";
                cnt++;
                idx = j;
                break;
            }
        }
    }
    cout << cnt;
    return 0;


}