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
        bool stopFlag = false;
        int Rcheck = 0;
        
        cin >> command;
        cin >> arrNum;
        cin >> a;

        for(int j = 1 ; j < a.size()-1;j++){
            string num ="";
            while(a[j]!=','){
                num+=a[j++];
            }
            if(num!="") numArray.push_back(stoi(num));
            
        }

        for(int cmd = 0 ; cmd < command.size();cmd++){

            if(command[cmd]=='R'){
                Rcheck++;
            }
            else{ 
            if(numArray.empty()){
                cout << "error"<<'\n';
                stopFlag = true;
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
        int cnt = 0 ;
        int size = numArray.size();
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
            if(cnt==size-1) cout << "]";
            else cout << ','; 
            cnt++;
        }
        if(stopFlag==0 && size==0) cout << "[]";
        cout << '\n';
    }

    
}
