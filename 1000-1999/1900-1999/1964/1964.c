#include<stdio.h>

int main(){
    long long int N;
    int sum = 0;
  
    scanf("%lld",&N);
    for(int i = 1 ; i<= N;i++){
        sum += (i*5-((i*2)-1))%45678;
        sum%=45678; // 값이 너무 커지므로 나눗셈 연산을 다시 한다. 
    // printf("%d\n",sum);
 
    }
    printf("%d",(sum+1)%45678);
    return 0;
  
}