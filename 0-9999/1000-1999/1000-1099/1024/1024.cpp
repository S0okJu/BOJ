#include<iostream>
using namespace std;

int main(){
    unsigned long M;
    int L;
    unsigned long num = 0;
    int firstValue = 0;

    cin >> M >> L;

    while(true){
        
        num = L*(L-1)/2;

        if( M>=num &&(M-num)%L == 0 ){
            firstValue = (M-num)/L;
            break;
        }
        else if( M < num){
            firstValue = -1;
            break;
        }                                                                                                                                        
        L++;
        
        
    }

    if(firstValue!= -1 && L<=100){
        for(int i = 0 ; i < L; i++){
            cout << firstValue++<< ' ';
        }    
    }
    else{
        cout << -1;
    }


    return 0;
}


