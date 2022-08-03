#include<iostream>
#include<sstream>
#include<algorithm>
#include<string>
#include<map>
using namespace std;

string works[7] = {"Re","Pt","Cc","Ea","Tb","Cm","Ex"};

int main()
{

    map<string,int> mapset;
    string a;
    int total = 0;

    while(getline(cin,a))
    {
        stringstream st(a);
        while(st >> a){
            mapset[a]++;
            total++;
        }
        
    }

    for(int i = 0 ; i < 7;i++)
    {
        double rate = mapset[works[i]]/(double)total;

        cout << works[i] << " " <<mapset[works[i]]<<" ";
        cout << fixed;
        cout.precision(2);
        if(rate == 0){
            cout << "0.00" <<"\n";
        } 
        else{
            cout << rate<<"\n";   
        }
    }
    cout << "Total"<<" "<<total<<" "<<"1.00";
    return 0;
}

/*
Cc Pt Pt Re Tb Re Cm Cm Re Pt Pt Re Ea Ea Pt Pt Pt Re Re Cb Cb Pt Pt Cb

*/