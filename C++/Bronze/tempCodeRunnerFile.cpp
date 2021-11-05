#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int functionMax(int a, int b){
    return a > b ? a : b;
}

int main(){
    int N, M;
    int maxValue = -1;
    int sum = 0;
    vector <int> game;
    cin >> N >> M;
    
    for(int i = 0 ; i < N; i++){
        int a;
        cin >> a;
        game.push_back(a);
    }

    sort(game.begin(),game.end());

    for(int firstCard = 0 ; firstCard < N-2; firstCard++){
        sum = 0;
        sum += game[firstCard];
        for(int secondCard = firstCard+1; secondCard < N-1; secondCard++){
            sum = game[firstCard];
            sum += game[secondCard];

            for(int thirdCard = secondCard+1; thirdCard < N; thirdCard++){
                
                if(sum + game[thirdCard] <= M){
                    maxValue = functionMax(maxValue, sum+ game[thirdCard]);
                    
                }
            }
        }
    }

    cout<< maxValue;

    return 0;
}