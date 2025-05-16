#include<iostream>
#include<algorithm>
#include<string>
#include<cmath>
#include<map>
using namespace std;

int main(){
    map<string,int> color;
    string input[3];
    color.insert({"black",0});
    color.insert({"brown",1});
    color.insert({"red",2});
    color.insert({"orange",3});
    color.insert({"yellow",4});
    color.insert({"green",5});
    color.insert({"blue",6});
    color.insert({"violet",7});
    color.insert({"grey",8});
    color.insert({"white",9});

    for(int i = 0 ; i < 3 ;i++){
        cin >> input[i];
    }
    long long int ans =(color[input[0]]*10 + color[input[1]])*pow(10,color[input[2]]);
    cout <<ans;
    return 0;
}