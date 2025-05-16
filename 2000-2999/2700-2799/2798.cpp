#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int functionMax(int a, int b){
    return a > b ? a : b;
}

int main(){
    int N, M;
    int maxValue = -1; // 초기화 
    int sum = 0;
    vector <int> game;
    cin >> N >> M;
    
    for(int i = 0 ; i < N; i++){
        int a;
        cin >> a;
        game.push_back(a);
    }

    sort(game.begin(),game.end()); // 구하기 쉽게 정렬을 해준다. 

    for(int firstCard = 0 ; firstCard < N-2; firstCard++){
        sum = 0; // 새로운 maxValue를 구하므로 다시 초기화해준다. 
        sum += game[firstCard];
        
        for(int secondCard = firstCard+1; secondCard < N-1; secondCard++){
            sum = game[firstCard];// 새로운 maxValue를 구하므로 다시 초기화 해준다. 
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