#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<pair<int,string>> people;
int price[100001];

int main(){

    fill(&price[0],&price[100001],0);
    int U, N;
    vector<pair<string,int>> v;

    cin >> U >> N;
    
    for(int i = 0 ; i< N;i++){
        string a;
        int b;
        cin >> a >> b;
        v.push_back({a,b});
        price[v[i].second]++;
    }

    int small = 100001;

    for(int i = 1; i <=100000;i++){
        if(price[i]>0){
            small = min(small,price[i]);
        }
    }

    vector<int> lowPrice;

    for(int i = 1; i<=10000;i++){
        if(price[i]==small){
            lowPrice.push_back(i);
        }
    } 

    sort(lowPrice.begin(),lowPrice.end());

    for(int i = 0 ; i<N;i++){
        if(v[i].second==lowPrice[0]){
            cout << v[i].first<<" "<<v[i].second;
            break;
        }
    }


    return 0;
}