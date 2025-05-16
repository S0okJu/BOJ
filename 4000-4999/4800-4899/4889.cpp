#include<iostream>
#include<string>
#include<stack>
using namespace std;

int main(){
    int idx = 1;

    while(true){
        string a;
        stack<char> st;
        int change = 0;
        cin >> a;

        if(a[0]=='-'){
            break;
        }
        
        for(size_t i = 0 ; i < a.length();i++){
            if(a[i]=='{'){
                st.push('{');
            }
            else{
                if(!st.empty()){
                    st.pop();
                }
                else{
                    change++;
                    st.push('{');
                }
            }
        }

     
        if(st.empty()){
            cout << idx<<". "<<change<<'\n';
        }
        else{
            cout << idx<<". "<<change+(st.size()/2)<<'\n';
        }
        idx++;
    }
    return 0;
}