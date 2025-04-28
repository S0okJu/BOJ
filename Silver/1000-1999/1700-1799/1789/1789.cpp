#include<iostream>
#include<cmath>
using namespace std;

// solution 1
int main(){
    long long int s;
    cin >> s;
    long long int m = sqrt(2*s);

    while(m*(m+1) > 2*s){
        m-=1;
    }

    cout << m;
    return 0;
}

// solution 2
int main(){
    long long int s;
    long long int result;
    cin >> s;

    for(int i = 1; i < s+1;i++){

        if(s-i<0){
            break;
        }
        s-=i;
        result = i;
        cout << "i: "<<i<<'\n';
        cout << "s: "<<s<<'\n';
        cout<<"--------"<<'\n';
    }
    cout << result;
    return 0;
}