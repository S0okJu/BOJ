#include<iostream>
using namespace std;

int problems[101];
int main(){
    int N;
    int score=0;
    int sum = 0;
    cin >> N;

    for(int i = 0 ; i < N;i++){
        cin >> problems[i];
        if(problems[i]!=0){
            sum+=++score;
        }
        else{
            score = 0;
        }
    }
    cout << sum;
    return 0;

}