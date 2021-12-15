#include<iostream>
using namespace std;

int main(){
    int snackPrice, snackNum, ownMoney;
    cin >> snackPrice >> snackNum >> ownMoney;

    if((snackPrice * snackNum)> ownMoney){
        cout << (snackPrice * snackNum) - ownMoney;
    }
    else{
        cout<<0;
    }

    return 0;
}