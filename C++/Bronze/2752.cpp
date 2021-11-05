#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
using namespace std;

int main(){
    vector<int> num;
    int a, b, c;
    cin >> a >> b >> c;
    num.push_back(a);
    num.push_back(b);
    num.push_back(c);

    sort(num.begin(),num.end());

    for(int i = 0 ; i < 3;i++){
        cout << num[i]<<" ";
    }

    return 0;
}