#include<iostream>
#include<string>
using namespace std;

string strList[7]={"c=","c-","d-","lj","nj","s=","z="};

int main(){
    string a;
    int len = 0;
    bool checkList = true;
    int start = 0; // 문자열의 인덱스를 표현하기 위해 

    cin >> a;

    while(true){
        checkList = false;
        if(start+2 <= a.size()){
            for(int i = 0 ;i<7;i++){
                if(a.substr(start,2)==strList[i]){
                    checkList = true;
                    len++;
                    start+=2;
                    break;
                }
            }
        }
        if(start+3 <=a.size()){
            if(a.substr(start,3)=="dz="){
                checkList = true;
                len++;
                start+=3;
            }
        }
        if(start+1<=a.size()&&checkList == false){
            start+=1;
            len++;
        }
        if(start==a.size())break; 
    }

    cout << len;

    return 0;
}