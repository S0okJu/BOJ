#include<iostream>
#include<string.h>
using namespace std;

int main(){
    int T;
    cin>> T;

    for(int i = 0 ; i  < T;i++){
        long int num[101];
        memset(num,0,101*sizeof(long int));
        num[1]= num[2]=num[3]=1;
        int a;
        cin >> a;
        for(int j=4;j<=a;j++){
            num[j] = num[j-2]+num[j-3];
        }
        cout << num[a]<<'\n';
    }
    return 0;
}