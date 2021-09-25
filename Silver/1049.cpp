#include<iostream>
using namespace std;

int main(){
    int N, M;
    int package, indi;
    int minPack = 1001;
    int minind = 1001;
    int res = 0;
    cin >> N >> M;

    for(int i = 0 ; i < M ;i++){
        cin >> package >> indi;
        minPack = minPack >= package ? package : minPack;
        minind = minind >= indi ? indi: minind;
    }

    while(true){
        if(N >= 6){ // N > 6 경우
            if(minPack < (minind*6))res += minPack;
            else res += minind*6;
            N-=6;
        }
        else if( N < 6 && N !=0){  // N < 6이면서 N != 0인 경우  
            if(minPack < (minind * N)) res += minPack;
            else res +=(minind * N);

            break;
        }
        else{ // N = 0인 경우
            break;
        }
    }

    cout << res;
    return 0;
}