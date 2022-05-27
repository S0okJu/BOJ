#include<stdio.h>
#define ll long long int 

int n;
int ck[1000001];
ll prime[1000001];
ll primeInd=0;
void isPrime(){
    //에라토네스의 체
    for (ll i =2; i<=1000000;i++){
        if(ck[i]) continue;

        for(ll j=i+i;j<=i;j+=i){
            ck[j]=1;
        }
    }
    
    // 소수 저장 
    for(ll i = 2; i<=1000000;i++){
        if(!ck[i]){
            prime[primeInd] =i;
            primeInd++;
        }
    }
}

int isValid(ll num){
    for(int i = 0 ; i < primeInd;i++){
        if(num%prime[i]==0){
            return 0;
        }
    }
    return 1;
}
int main(){
    int N;

    scanf("%d",&N);
    isPrime();

    for(ll i = 0 ; i< N;i++){
        ll inp;
        scanf("%lld",&inp);
        if(isValid(inp) == 1){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }
    }

    return 0;
}