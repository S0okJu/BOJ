#include<iostream>
#include<string>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    string S;
    int N, M;
    int count = 0;

    cin >> N;
    cin >> M;
    cin >> S;


    for(int i = 0 ; i < M;i++){
        
        if(S[i]=='O') continue;
        else{
            int cntP = 0;

            while(S[i+1]=='O' && S[i+2]=='I'){

                cntP++;
                if(cntP==N){
                    cntP--;
                    /* 중복 카운트를 막기 위해서
                    IOIOIOIO N=3인 경우
                    연속으로 OI가 4개 있는 경우 중복을 없애기 위해 cntP--을 해준다.
                    */ 
                    count++;
                }
                
                i+=2; // IO을 건너뛰기 위해서 

            }
        }
    }
    cout << count;
    return 0;
}