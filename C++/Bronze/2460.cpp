#include<iostream>
#include<algorithm>

int Findmax(int a, int b){
    return a > b ? a :b;
}

int main(){
    int train[10][2];
    int maxValue = -1;
    std::fill(&train[0][0],&train[10][2],0);

    for(int i = 0; i < 10;i++){
        std::cin >> train[i][0] >> train[i][1];
    }    

    int personOnBoard = train[0][1];
    for(int i = 1 ; i <10;i++){
        personOnBoard = personOnBoard-train[i][0]+train[i][1];
        maxValue = Findmax(maxValue, personOnBoard);
    }
    std::cout << maxValue;
}