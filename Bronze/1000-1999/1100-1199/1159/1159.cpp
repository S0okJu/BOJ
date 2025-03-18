#include<iostream>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
map<char,int> characterMap;
string player[151];

int main(){
    int N;
    bool check = false;
    cin >> N;

    for(int i = 0 ; i <N;i++){
        cin>> player[i];
        if(characterMap.find(player[i][0])==characterMap.end()){
            characterMap.insert({player[i][0],0});
        }
        characterMap[player[i][0]]++;

    }

    for(auto iter=characterMap.begin();iter!=characterMap.end();iter++){
        if(iter->second>=5){
            cout<<iter->first;
            check=true;
        }
    }
    if(check ==false){
        cout << "PREDAJA";
    }

    return 0;

}