#include<iostream>
using namespace std;

int main(){
    int* ryth = new int[8];
    int preryth = 0;
    int flag = 0;
    int preflag = 0;

    for(int i = 0 ; i < 8 ; i++){
        cin >> ryth[i];
    }
    preryth = ryth[0];

    if(ryth[0] == 1) preflag = 0;
    else if(ryth[0]==8) preflag = 1;
    else preflag = -1;

    for(int i = 1 ; i < 8 ; i++){
        
        if(preryth < ryth[i]){
            flag = 0;
        }
        else{
            flag = 1;
        }
        if(preflag != flag){
            flag = -1;
            break;
        }
        preflag = flag;
        preryth = ryth[i];
    }

    if(flag == 0) cout <<"ascending"<<endl;
    else if(flag == 1) cout << "descending"<<endl;
    else cout << "mixed"<<endl;

    delete[] ryth;
}