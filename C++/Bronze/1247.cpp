#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main(){
    for(int i = 0 ; i < 3;i++){
        int n, pidx = 0, midx = 0;
        long long int ans = 0;
        long long int p[100001]; // 양수인 경우
        long long int m[100001]; // 음수인 경우 
        
        cin >> n;

        for(int j = 0 ; j< n;j++){
            long long int input;
            cin >> input;

            if(input>0) p[pidx++]=input;
            else m[midx++] = input;
        }
        while(pidx > 0 && midx > 0){
            if(ans >0) ans+=m[--midx];
            else{
                ans+=p[--pidx];
            }
        }
        
        for(int i =0; i<pidx;i++){
            ans+=p[i];
            if(ans>0)break;
        }
        for(int i =0; i<midx;i++){
            ans+=m[i];
            if(ans<0)break;
        }
        if(ans ==0){
            cout << "0";
        }
        else{
            string outputStr = ans >0 ?"+":"-";
            cout <<outputStr;
        }
        cout << "\n";
    }
    return 0;
}