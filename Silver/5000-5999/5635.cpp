#include<iostream>
#include<string>
#include<algorithm>
#include<tuple>
#include<vector>
using namespace std;

bool cmp (tuple<string,int,int,int> &a, tuple<string,int,int,int> &b){
    int aDay = get<1>(a);
    int aMon = get<2>(a);
    int aYear =get<3>(a);

    int bDay = get<1>(b);
    int bMon = get<2>(b);
    int bYear =get<3>(b);

    if(aYear == bYear){
        if(aMon==bMon) return aDay > bDay;
        return aMon > bMon;
    }
    return aYear > bYear;
}

int main(){
    int N;
    vector<tuple<string,int,int,int>> student;
    cin >> N;

    for(int i = 0 ; i < N;i++){
        int d,m,y;
        string name;
        cin >> name >> d >> m >> y;
        student.push_back({name,d,m,y});
    }
    sort(student.begin(),student.end(),cmp);
    cout << get<0>(student[0])<<'\n'<<get<0>(student[N-1]);
    return 0;
}