#include<iostream>
#include<algorithm>
#include<vector>
#include<utility>
using namespace std;

bool compare(pair<int,int> a, pair<int,int> b){
    if(a.first == b.first){
        return a.second < b.second;
    }
    else return a.first < b.first;
}
int main(){
    int N;
    vector<pair<int,int>> input;
    vector<pair<int, int> >::iterator iter;

    cin >> N;

    for(int i = 0 ; i < N; i++){
        int x, y;
        cin >> x >> y;
        input.push_back(make_pair(x,y));
    }

    sort(input.begin(), input.end(),compare);

    for(iter = input.begin(); iter!=input.end();iter++){
        cout << iter->first << " " << iter->second  << endl;

    }

    return 0;
}


