#include<iostream>
#include<algorithm>
using namespace std;

int main(){
    int sum = 0;
    int minV = 101;
    for(int i = 0 ; i < 7 ;i++){
        int a;
        cin >> a;
        if(a %2 == 1){
            sum+=a;
            minV = min(minV,a);
        }
        
    }
    if(sum ==0) {
        cout << -1;
        return 0;
    }
    cout << sum << '\n'<< minV;
    return 0;

}