#include<iostream>
#include<stack>
using namespace std;



int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);

    int N;
    int first = 1001;
    int last, longest, pos, len, answer;
    int roof[1001];
    stack<int> storage;


    cin >> N;

    while(N--){
        cin >> pos >> len;
        roof[pos] = len;
        if(last < pos) last = pos;
        if(first > pos) first = pos;
        if(len > roof[longest]) longest = pos;

    }

    for(int i = first; i<= longest; i++){
        if(roof[i]){
            if(storage.empty()) storage.push(roof[i]);
            else if(roof[i]>storage.top()) storage.push(roof[i]);
            
        }
        answer += storage.top();
    }

    while(!storage.empty()) storage.pop();
    
    for(int i = last; i > longest; i--){
        if(roof[i]){
            if(storage.empty()) storage.push(roof[i]);
            else if(roof[i] > storage.top())storage.push(roof[i]);
        }
        answer+= storage.top();
    }
    cout << answer;
    return 0;
}
