#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

class student{
public:
    int country;
    int id;
    int score;
    student(int country, int id, int score){
        this->country = country;
        this->id = id;
        this->score = score;
    }
};

bool cmp(student a, student b);

int countryNum[1001];

int main(){
    int N;
    bool flag = true;
    cin >> N;
    vector<student> studentList;

    for(int i = 0 ; i < N;i++){
        int a, b, c;
        cin >> a >> b >> c;
        studentList.push_back(student(a,b,c));
    }

    sort(studentList.begin(),studentList.end(),cmp);

    int cnt = 0;
    for(int i = 0 ; i < N;i++){
        if(countryNum[studentList[i].country]<2){
            cout << studentList[i].country << " "<<studentList[i].id<<"\n"; 
            cnt++;
        }
        countryNum[studentList[i].country]++;
        if(cnt==3)break;
    }
    return 0;
}

bool cmp(student a, student b){
    if(a.score > b.score){
        return true;
    }
    return false;
}