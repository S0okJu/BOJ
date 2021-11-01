#include<iostream>
#include<stack>
#include<vector>
using namespace std;

int n, a[100001];
stack<int> st;
vector<char> ans;

int main(){
    int pos = 0;
    vector<char>::iterator iter; 
    cin >> n;

    for(int i = 0 ; i< n; i++) cin >>a[i];

    for(int i = 1; i<=n;i++){
        st.push(i);
        ans.push_back('+');

        while(!st.empty()&&st.top()==a[pos]){
            st.pop();
            ans.push_back('-');
            pos++;
        }
        
    }

    if(!st.empty()){
        cout<<"NO";
        return 0;
    }
    else{
        for(iter=ans.begin();iter!=ans.end();iter++){
            cout << *iter<<'\n';
        }
    }


    return 0;
}