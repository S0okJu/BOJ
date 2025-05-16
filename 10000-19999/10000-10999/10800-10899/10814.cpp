#include<iostream>
#include<vector>
#include<algorithm>
#include<utility>
#include <string>
using namespace std;
bool compare(pair<int,string> a, pair<int,string> b){
    if(a.first == b.first) return false;
    else return a.first < b.first;
}
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    vector<pair<int, string>> student;
    vector<pair<int,string>>::iterator iter;
    
    cin >> N;

    for(int i = 0 ; i < N; i++){
        int num;
        string name;
        cin >> num >> name;
        student.push_back(make_pair(num,name));
    }
    stable_sort(student.begin(), student.end(),compare);

    for(iter = student.begin(); iter!=student.end();iter++){
        cout << iter->first<<" "<<iter->second<<'\n';
    }


    return 0;
}