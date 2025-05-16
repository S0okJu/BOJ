#include<iostream>
#include<map>
#include<string>
using namespace std;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M;
    map<string, int> poketmonNum;
    map<int, string> poketmon;
    cin >> N >> M;

    for(int i = 0 ; i < N; i++){
        string p;
        cin >> p;
        poketmonNum[p]=i;
        poketmon[i] = p;

    }
    
    for(int j = 0 ; j <M;j++){;


        string name;
        cin >> name;

        if(name[0]>=48 && name[0]<=57){
            int idx = stoi(name);
            cout << poketmon[idx-1]<<'\n';
        }
        else{
            cout<<poketmonNum[name]+1<<'\n';
        }
    }


    return 0; 
}