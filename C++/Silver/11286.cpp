#include<iostream>
#include<queue>
#include<iostream>
#include<cmath>
#include<functional>
using namespace std;


int main()
{
    int N;
    priority_queue<pair<int,int>, vector<pair<int,int>>,greater<pair<int,int>>> q;
    cin >> N;

    for(int i = 0 ; i < N ;i++)
    {

        int x;
        cin >> x;

        if(x!=0){
            if(x < 0)
            {
                q.push({abs(x),-1});
            }
            else
            {
                q.push({abs(x),1});
            }
        }
        else
        {
            if(q.empty()){
                cout <<"0"<<'\n';
            }
            else{
                cout << "pop: "<< q.top().first * q.top().second<<'\n';
                q.pop();
            }

        }
    }
    return 0;
}