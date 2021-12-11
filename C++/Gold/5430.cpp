#include<iostream>
#include<string>
#include<deque>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int i = 0 ; i <  T;i++){
        deque<int> numArray;
        string a;
        string command;
        int arrNum;
        int stopFlag = 0;
        int Rcheck = 0;
        
        cin >> command>>arrNum>>a;

        for(int j = 1 ; j < a.size();j++){
            string num ="";
            while(a[j]!=','&&a[j]!=']'){
                num+=a[j++];
            }
            if(num!="") numArray.push_back(stoi(num));
            
        }// 문자열에서 숫자형만 deque에 넣는다. 

        for(int cmd = 0 ; cmd < command.size();cmd++){

            if(command[cmd]=='R'){
                Rcheck++;
            }
            else{ 
                if(numArray.empty()){
                    cout << "error";
                    stopFlag = 1;
                    break;

                }  

                if(Rcheck%2 == 0){
                    numArray.pop_front();
                }
                else{
                    numArray.pop_back();
                }
            }
        }
        /*
        RCheck가 짝수인 경우 두번 뒤집으므로(다시 제자리) 맨 첫칸에서부터 시작한다.
        */

       // 형식에 맞게 출력하기
        int cnt = 0 ;
        int Numsize = numArray.size();
        while(numArray.size()){
            if(cnt==0) cout << "[";

            if(Rcheck % 2 == 0){
                cout << numArray.front();
                numArray.pop_front();
            }

            else{
                cout << numArray.back();
                numArray.pop_back();
            }
            if(cnt==Numsize-1) cout << "]";
            else cout << ','; 
            cnt++;
        }
        if(stopFlag==0 && Numsize==0) cout << "[]";
        cout << '\n';
    }

    return 0;
    
}
