#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>
using namespace std;

int main(){
    int N;
    int count = 0;
    vector<pair<int,int>> person;
    cin >> N;


    for(int i = 0 ;i < N; i++){
        int a, b;
        cin >> a>>b;
        person.push_back(make_pair(a,b));
    }

    for(int i = 0 ; i < N;i++){
        count = 0;
        for(int j = 0 ;j<N;j++){
            if(i!=j){
                if(person[i].first < person[j].first && person[i].second < person[j].second){
                    count++;
                }
            }
            else continue;
        }
        cout << count+1<< " ";
        
    }


    return 0;
}