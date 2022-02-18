#include<iostream>
using namespace std;

long long int dp[100001][8];
const long long int divNum = 1'000'000'007;
int main(){
    int D;

    dp[0][0]=1;

    cin >> D;

    for(int i = 1 ; i <= D;i++){
        dp[i][0] = dp[i-1][1] + dp[i-1][2];
        dp[i][1] = dp[i-1][0]+dp[i-1][2]+dp[i-1][3];
        dp[i][2] = dp[i-1][1] + dp[i-1][3] + dp[i-1][4]+dp[i-1][0];
        dp[i][3] = dp[i-1][4] + dp[i-1][1]+dp[i-1][2]+dp[i-1][5];
        dp[i][4] = dp[i-1][3]+dp[i-1][2]+dp[i-1][5]+dp[i-1][7];
        dp[i][5] = dp[i-1][3]+dp[i-1][4]+dp[i-1][6];
        dp[i][6] = dp[i-1][5] + dp[i-1][7];
        dp[i][7] = dp[i-1][4] + dp[i-1][6];
        
        dp[i][0]%=divNum;
        dp[i][1]%=divNum;
        dp[i][2]%=divNum;
        dp[i][3]%=divNum;
        dp[i][4]%=divNum;
        dp[i][5]%=divNum;
        dp[i][6]%=divNum;
        dp[i][7]%=divNum;

    }
    cout << dp[D][0]%divNum;
    return 0;
}


/*
?? 1000000007 왜 나눌까? 

1000000007, 1000000009 와 같은 수로 나눈 나머지를 답으로 제출하라고 하는 문제가 종종 있는데, 
이 수는 소수이고 어떤 답에 대한 해시값을 출력하라는 의미이다.
C에서는 수가 커지면 int overflow를 방지하기 위한 방법으로 나머지 출력하라고 하는 경우고 있는데,
파이썬은 수의 범위가 어느정도 크기때문에 마지막에 나눠주면 된다. (C, Java의 경우 각 연산에 대하여 나머지를 연산 필요)
하지만 속도 측면에서 나눗셈연산이 상당히 무거워서 나눗셈 연산을 많이 하는게 좋은 방법은 아니지만
속도면에서 미리 나눗셈 연산을 해주면 나중에 큰 수의 나눗셈을 수행하는 것 보다 효율적인 결과를 볼 수 있다. 

출처: https://data-make.tistory.com/401 [Data Makes Our Future]

*/