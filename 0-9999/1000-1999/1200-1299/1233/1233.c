#include<stdio.h>

int addSum[81];
int main(){
    int s1, s2, s3;
    int ans; 
    scanf("%d %d %d", &s1,&s2,&s3);

    for(int s1_rot = 1; s1_rot<=s1;s1_rot++){
        for(int s2_rot = 1; s2_rot<=s2;s2_rot++){
            for(int s3_rot=1; s3_rot<=s3;s3_rot++){
                addSum[s1_rot+s2_rot+s3_rot]++;
            }
        }
    }
    int maxNum = -1;

    for(int i = 3; i<=s1+s2+s3;i++){
        if(maxNum < addSum[i]){
            maxNum = addSum[i];
            ans = i;
        }
    }

    printf("%d",ans);
    return 0;
}