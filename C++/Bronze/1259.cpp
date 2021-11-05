#include<iostream>
#include<algorithm>
#include<string>
using namespace std;


int main(){


    while(true){
        int input;
        string useString;
        string revString;

        cin >> input;
        if(input ==0) break;

        useString = to_string(input);
        revString = useString;
        reverse(revString.begin(),revString.end());

        if(useString == revString){
            cout << "yes"<<'\n';
        }
        else cout << "no"<<'\n';

    }

    return 0;
}
