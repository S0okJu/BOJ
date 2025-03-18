#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    string s;
    int arr[3];
    int idx= 0;
    cin >> s;
    
    idx = s.find('/');
    arr[0]=stoi(s.substr(0,idx));

    int before = idx;
    idx = s.find('/',before+1);
    arr[1] = stoi(s.substr(before+1,idx - before-1));

    arr[2]=stoi(s.substr(idx+1));
    
    if(arr[0]+arr[2]<arr[1]||arr[1]==0){
        cout << "hasu";
    }
    else{
        cout <<"gosu";
    }
    
    return 0;
}