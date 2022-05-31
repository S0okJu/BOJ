#include <iostream>
#include <algorithm>
using namespace std;

int minArr[50001];
int maxArr[50001];

int main(){
    int N;
    int ans;
    cin >> N;

    for(int i = 0 ; i < N;i++){
        int a, b;
        cin >> a >> b;

        minArr[i] = a-b;
        maxArr[i] = a+b;

    }
    
    sort(minArr,minArr+N);
    sort(maxArr,maxArr+N);

    ans = max(minArr[N-1]-minArr[0],maxArr[N-1]-maxArr[0]);
    cout << ans;
    return 0;
}
