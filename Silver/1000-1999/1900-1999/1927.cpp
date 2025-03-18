#include<iostream>
#include<queue>
#include<algorithm>
#include<functional> // greater, less 
using namespace std;

int n;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;

    priority_queue<int, vector<int>,greater<int>>pq;
    while(n--){
        int x;
        cin >> x;
        if (x ==0){
            if(pq.empty()){
                cout << "0"<<'\n';
            }
            else{
                cout << pq.top()<<'\n';
                pq.pop();
            }
        }
        else pq.push(x);
    }

    return 0;
}