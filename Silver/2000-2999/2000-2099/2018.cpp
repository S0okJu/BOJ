#include<iostream>
using namespace std;

int main(){
    int N;
    int first = 0;
    int cnt = 0;
    cin >> N; 
    int tmp = N;

    for(int i = 1; i <=N;i++){
        first +=i;
        if(tmp>=first){
            if((tmp-first)%i==0){
                cnt++;
            }
        }
        else{
            break;
        }
    }
    cout << cnt;
    return 0;
}
