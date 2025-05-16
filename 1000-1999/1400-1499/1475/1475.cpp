#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main(){
    string a;
    int sets = -1;
    int sixNine = 0;
    int setNum[10];
    fill(&setNum[0],&setNum[10],0);

    cin >> a;

    if(a.size() == 1){
        cout << 1;
        return 0;
    }
    else{
        for(int i = 0 ; i < a. size();i++){
            setNum[a[i]-'0']++;
        }

        for(int i =0;i<a.size();i++){
            if((a[i]-'0')!=6 && (a[i]-'0')!=9){
                sets = max(sets , setNum[a[i]-'0']);
            }
        }
        if((setNum[6]+setNum[9])%2==1){
            sixNine = (setNum[6]+setNum[9])/2+1;
        }
        else{
            sixNine=(setNum[6]+setNum[9])/2;
        }
        sets = max(sets,sixNine);
        cout <<sets;
    }
    return 0;
}