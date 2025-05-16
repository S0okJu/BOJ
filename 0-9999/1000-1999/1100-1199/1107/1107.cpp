#include<iostream>
#include<cmath> // 절댓값을 사용하기 위해 
#include<algorithm>
using namespace std;
int n, m, ans;
int cnt;
const int start = 100;
bool broken[10];

int moveNum(int num){
    // 0인 경우
    if(num==0){
        if(broken[num]) return -1;
        return 1;
    }
    // 숫자로 이동 가능한 경우
    int len = 0 ;
    while(num>0){
        if(broken[num%10]) return -1;
        len++;
        num/=10;
    }
    return len;

}
int main(){
    int tmp;
    cin >> n;
    cin >> m;
    for(int i = 0 ; i < m ;++i){
        cin >> tmp;
        broken[tmp] = true;
    }

    // 가고자 하는 채널이 같다면
    if(n==start){
        cout << 0 <<'\n';
        return 0;
    }
    
    // +,-으로만 이동하는 경우 
    ans = abs(n-start);
    for(int i = 0 ; i < 1'000'000;++i){
        cnt = moveNum(i); // 숫자 버튼으로 가능한 경우 
        if(cnt>0){
            cnt += abs(n-i); // 숫자버튼 + +/- 이동
            ans = min(cnt,ans);
        }
    }
    cout << ans<<'\n';
    return 0;
}