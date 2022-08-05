#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int main()
{
    string N;
    cin >> N;

    int pre_plus_len = N.length()-1;
    long long int ans = 0;
    long long int final_mul = 0;
    for(int i = 0 ;i < pre_plus_len;i++){
        ans +=((9*pow(10,i))*(i+1));
        // cout << ans << "\n";
    }

    if(pre_plus_len-1 >= 0){
        final_mul = 9*pow(10,pre_plus_len-1);
    }

    ans+=((stol(N)-pow(10,pre_plus_len)+1)*(pre_plus_len+1));

    cout << ans;
    return 0;
}


