#include<iostream>
#include<string>
using namespace std;


int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    string A, B;
    long long sum = 0;
    cin >> A >> B;

    for(int a = 0 ; a < A.size();a++){
        for(int b = 0 ; b<B.size();b++){
            sum +=(A[a]-'0')*(B[b]-'0');
        }
    }

    cout << sum;

    return 0;
}
