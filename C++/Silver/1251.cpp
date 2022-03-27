#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    string N;
    vector<string> group;
    cin >> N;

    for(string::size_type i = 1; i< N.length()-1;i++){
        for(string::size_type j =i+1;j<N.length();j++){
            string f = N.substr(0,i);
            string s = N.substr(i,j-i);
            string t = N.substr(j);
            
            reverse(f.begin(),f.end());
            reverse(s.begin(),s.end());
            reverse(t.begin(),t.end());
            string input = f+s+t;
            group.push_back(input);
        }

    }
    sort(group.begin(),group.end());
    cout << group[0];
    return 0;

}