#include<stdio.h>

long long sum(long long n){
    long long cnt[10]={0,};
    long long firstPlace, lastPlace,digit=1;
    long long sum = 0;
    if(n<=0){
        return 0;
    }
    while(n>0){
        firstPlace = n/(digit*10);
        lastPlace = n %(digit*10);

        // 일의 자리 수부터 cnt
        for(int i = 0 ; i<10;i++){
            cnt[i] += firstPlace*digit;
        }
        for(int i = 1; i <=lastPlace/digit ;i++){
            cnt[i] += digit;
        }
        // 그 앞의 자리 수 cnt
        // 가장 윗 자리수의 앞의 자리 숫자의 자릿수 개수를 더함. 
        cnt[(lastPlace/digit+1)%10] += lastPlace%digit;
        n-=9*digit;
        digit*=10;

    }
    for(int i = 1 ; i < 10;i++){
        sum +=(i*cnt[i]);
    }
    return sum;
}


int main(void){
    long long L, U;
    long long calc;
    scanf("%lld %lld",&L, &U);

    calc = sum(U)-sum(L-1);
    printf("%lld",calc);
    return 0;
}