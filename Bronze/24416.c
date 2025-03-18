#include<stdio.h>

int fibCnt = 0;
int f[81];

int fib(int n){
    if (n==1 || n==2){
        return 1;
    }
    else{
        fibCnt++;
        return (fib(n-1) +fib(n-2)); 
    }
}

int fibonacci(int n){
    f[1]=f[2]=1;

    for(int i = 3; i <=n;i++){
        f[i] = f[i-1]+f[i-2];
    }
    return f[n];
}

int main(void){
    int n;
    scanf("%d",&n);

    int recurCnt = fib(n);
    printf("%d %d", recurCnt,n-2);

    return 0;
}