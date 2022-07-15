#include<iostream>
#include<string>
using namespace std;

int main(){
    string fan = "fan";
    string input;
    string ans;

    cin >> input;

    for(int i = 0 ; i<3;i++){
        ans="";
        for(int j = 0 ; j< 3;j++){
            ans+=":";
            if(i==1 && j==1){
                ans+=input;
            }
            else{
                ans+=fan;
            }
            ans+=":";
        }
        cout<< ans<<"\n";
    }
    
}