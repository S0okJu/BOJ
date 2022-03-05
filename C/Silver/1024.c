#include<stdio.h>
#include<stdbool.h>

int main(){
    long long int N;
    int L;
    long long int firstValue;
 
    scanf("%lld %d", &N, &L);

    while(true){
        long long int tmp = (L-1)*L/2;

        if(N >= tmp && (N-tmp)%L==0){
            firstValue = (N-tmp)/L;
            break;
        }
        else if(N< tmp){
            firstValue = -1;
            break;
        }
        L++;
    }

    if(L<=100 && firstValue!=-1){
        for(int i = 0 ; i < L; i++){
            printf("%lld ",firstValue++);
        }
    }
    else{
        printf("%d",-1);
    }
    return 0;
}