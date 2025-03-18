#include<iostream>
using namespace std;

long long calc(long long int n){
    long long int c[10] = {0,},s=1,sum=0,t,r;
    if(n<=0)return 0;
    while(n>0){
        t = n/(s*10);
        r = n%(s*10);
        for(int i = 0 ; i < 10; i++){
            c[i] +=t*s;
        }

        for(int j = 1 ; j <=(r/s);j++){
            c[j] +=s;
        }

        c[(r/s+1)%10] +=r%s;
        n-=9*s;
        s*=10; // 자릿수 갱신 
    }
    for(int i = 1; i < 10; i++){
        sum += i*c[i];
    }
    return sum;
}

int main(){
    long long int L,U;
    long long int sum;
    cin >> L >> U;
    
    sum = calc(U)-calc(L-1);
    cout << sum;
    return 0;

}

