#include<iostream>
#include<vector>
using namespace std;

int main(){
    int cntI = 0, cntJ=0;
    int n, m;
    cin >> n >> m;
    
    string *kingdom = new string[n];
    vector<int> countI(n);
    vector<int> countJ(m);

    for(int i = 0 ; i < n; i++ ){
        cin >> kingdom[i];
        
        for(int j = 0 ; j < m;j++){
            if(kingdom[i][j]=='X'){
                countI[i]++;
                countJ[j]++;
            }
        }
    }

    for(int i = 0 ; i < n; i++){
        if(countI[i]==0){
            cntI++;
        }
    }

    for(int j = 0 ; j < m; j++){
        if(countJ[j]==0){
            cntJ++;
        }
    }

    if(cntI > cntJ){
        cout << cntI;
    }
    else{
        cout << cntJ;
    }
    delete[] kingdom;
    return 0;
    
}