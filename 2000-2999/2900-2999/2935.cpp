#include<iostream>
#include<string>
using namespace std;

int main(){
    string a,op,b;
    cin >> a >> op >> b;

    int lenA = a.length();
    int lenB = b.length();

    if(op=="*"){
        cout << "1";
        for(int i=0;i<(lenA+lenB)-2;i++){
            cout<<"0";
        }
        
    }
    else{
        
        if(lenA >= lenB){
            a[lenA-lenB]++;
            cout << a;
        }
        else{
            b[lenB-lenA]++;
            cout<<b;
        }
    }
    return 0;

}