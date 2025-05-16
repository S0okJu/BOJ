#include<iostream>
#include<string>
using namespace std;

int main(){
    while(true){
        string a;
        int ans = 1;

        cin >> a;
        if(a=="0") break;
        for(size_t i = 0 ; i < a.size();i++){
            if(a[i]=='0'){
                ans+=5;
            }
            else if(a[i]=='1'){
                ans+=3;
            }
            else{
                ans +=4;
            }

        }
        cout<<ans<<'\n';
    }
    return 0;
}