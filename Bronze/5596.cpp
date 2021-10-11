#include<iostream>
using namespace std;

class subject{
    int inf;
    int math;
    int sci;
    int eng;
public:
    subject(){
        inf = 0;
        math = 0;
        sci = 0;
        eng = 0;
    }
    subject(int inf, int math, int sci, int eng){
        this->inf = inf;
        this->math = math;
        this->sci = sci;
        this->eng = eng;
    }
    int sum(){
        return inf + math + sci + eng;
    }

};
int main(){
    int information, math, science, english;

    cin >> information >> math >> science >> english;
    subject T(information,math,science,english);

    cin >> information >> math >> science >> english;
    subject S(information,math,science,english);
    
    if(T.sum()< S.sum()){
        cout << S.sum();
    }
    else cout << T.sum();

    return 0;
}