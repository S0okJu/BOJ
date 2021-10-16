#include<iostream>
#include<algorithm>
using namespace std;

int wine[10001];
int amount[10001];

int main(){

    int n;
    
    cin >> n;

    for(int i = 1;i<=n;i++){
        cin >> amount[i];
    }


    wine[1] = amount[1];
    wine[2] = amount[1] + amount[2];
    for(int i = 3; i<=n;i++){
        wine[i] = wine[i-1];
        wine[i] = max(wine[i],wine[i-2]+amount[i]);
        wine[i] = max(wine[i],wine[i-3]+amount[i-1]+amount[i]);
    }

    cout << wine[n];
   
    

    return 0;
}