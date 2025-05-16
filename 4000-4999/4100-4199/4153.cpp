#include<iostream>
using namespace std;

int max(int a, int b){
    return a > b ? a : b;
}
int main(){
    unsigned int a, b, c = 0;
    bool correct;
    while(true){
        int maxValue = 0;
        
        cin >> a >> b >> c;
        if(a == 0 && b == 0 && c == 0) break;
        maxValue = max(max(a,b), c);

        if(maxValue == a){
            if((b*b)+(c*c) == maxValue*maxValue) correct = true;
            else correct = false;
        }
        else if(maxValue == b){
            if((a*a)+(c*c) == maxValue*maxValue) correct = true;
            else correct = false;
        }
        else{
            if((a*a)+(b*b) == maxValue*maxValue) correct = true;
            else correct = false;
        }
        if(correct == true)cout << "right"<<endl;
        else cout << "wrong"<<endl;
        

    }

    return 0;
}