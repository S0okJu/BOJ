#include<iostream>
#include<string>
using namespace std;

string name[51];

int main(){
    int N;
    string answer="";
    cin >> N;
    
    // N=1인 경우
    if(N == 1){
        cin >> name[0];
        cout <<name[0];
        return 0;
    }
    for(int i = 0 ; i <N;i++){
        cin >> name[i];
    }

    for(int i = 0 ; i< name[0].size(); ++i){
        bool check= false;
        char c = name[0][i];
        for(int j = 1 ; j < N; ++j){
            if(c == name[j][i]) check = true; 
            else {
                check = false;
                break;
            }
        }

        if(check == true) answer+=name[0][i];
        else answer+='?';
    
    }

    cout << answer;
    return 0;


}