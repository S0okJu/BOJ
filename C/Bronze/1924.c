#include<stdio.h>

int main(){
    int mon, day;
    int ans=-1;
    const char* dayName[7]={"MON","TUE","WED","THU","FRI","SAT","SUN"};
    int daycnt[12]={31,28,31,30,31,30,31,31,30,31,30,31};

    scanf("%d %d",&mon,&day);

    for(int i = 0 ; i < mon-1;i++){
        for(int j = 0 ; j < daycnt[i];j++){
            ans++;
            if(ans%7==0){
                ans%=7;
            }
        }
    }
    for(int check_d = 0 ; check_d<day;check_d++){
        ans++;            
        if(ans%7==0){
            ans%=7;
        }
    }
    printf("%s",dayName[ans]);
    return 0;

}