#include<cstdio>

const int Max = 1000000;
int main(){
    int m,n;
    bool arr[Max+1];
    scanf("%d %d",&m,&n);

    arr[1] = true; //1은 제외되므로 true로 초기화 

    for(int i = 2 ;i*i<=Max;i++ ){
        if(!arr[i]){
            for(int j = (i*i)%Max;j<=Max;j+=i ){
                //j의 배수만큼 제거(true 값으로 변경)
                arr[j] = true;
            }
        }
    }

    for(int i = m; i <=n;i++){
        if(!arr[i]) printf("%d\n",i);
    }

    return 0;

    
}