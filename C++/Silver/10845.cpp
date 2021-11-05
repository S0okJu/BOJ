#include<iostream>
#include<queue>
#include<string>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
	cin.tie(0);
    cout.tie(0); 

    int N;
    string str;
    int pushValue;
    queue<int> q;

    cin >> N;
    for(int i = 0 ; i < N;i++){
        cin >> str;
        if(str == "push"){
            cin >> pushValue;
            q.push(pushValue);
        }
        else if( str=="pop"){
            if(q.empty()) cout << -1<<endl;
            else{
                cout << q.front()<<endl;
                q.pop();
            }
        }
        else if(str =="size") cout << q.size() << endl;
        else if( str =="front"){
            if(q.empty()) cout << "-1"<<endl;
            else{
                cout << q.front()<<endl;
            }
        }
        else if( str == "back"){
            if(q.empty()) cout << "-1"<<endl;
            else{
                cout << q.back()<<endl;
            }
        }
        else if(str == "empty"){
            if(q.empty()) cout << "1"<<endl;
            else cout << "0" << endl;
        }
    }

    return 0;
}