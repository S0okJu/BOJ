#include<stdio.h>
#include<string.h>

char vowel[10]= {'a','e','i','o','u','A','E','I','O','U'};
int main(){

    while(1){
        char inp[255];
        int cnt = 0;
        // fgets(inp,sizeof(inp),stdin);
        // \n -> \0 으로 변경 -> 있어도 없어도 결과는 똑같다. 
        // inp[strlen(inp)-1]='\0';
        gets(&inp);
        if(inp[0]=='#'){
            break;
        }

        for(int i = 0 ; inp[i]!='\0';i++){
            for(int vow_n = 0 ; vow_n <10; vow_n++){   
                if(inp[i]==vowel[vow_n]){
                    cnt++;
                    break;
                }
            }
        }
        printf("%d\n",cnt);
    }
    return 0;
}