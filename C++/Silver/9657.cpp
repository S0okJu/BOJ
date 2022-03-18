#include<iostream>
using namespace std;

int main(){
    int N;
    cin >> N;

    int game[1001];
    fill(&game[0],&game[1001],0);
    game[1]= game[3] = game[4] =1;

    for(int i = 5;i<=N;i++){
        if(!(game[i-1]&& game[i-3]&&game[i-4])){
            game[i] = 1;
        }
    }
    if(game[N]==1){
        cout << "SK";
    }
    else{
        cout << "CY";
    }
    return 0;
}

