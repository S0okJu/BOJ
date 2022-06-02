#include<stdio.h>

int FindMin(int a, int b){
    return a < b? a:b;
}
int main(){
    int N;
    scanf("%d",&N);

    for(int i = 0 ; i < N;i++){
        int arr[7];
        int sum = 0;
        int min= 101;
        for(int j = 0 ; j< 7; j++){
            scanf("%d",&arr[j]);
            
            if(arr[j]%2==0){
                sum+=arr[j];
                min = FindMin(min,arr[j]);
            }
        }
        printf("%d %d\n",sum, min);
    }

    return 0;
}