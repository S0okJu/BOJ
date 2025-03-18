#include<iostream>
using namespace std;

int main(){
    int a;
    int ans=0;
    int min = 2001;
    for(int i = 0 ; i < 5 ; i++){
        cin >> a;
        min = min > a ? a:min;
        if(i==2 || i==4){
            ans+=min;
            min = 2001;
        }
    }

    cout << ans-50;
    return 0;
}