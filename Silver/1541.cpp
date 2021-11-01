#include<iostream>
#include<string>
using namespace std;

int num[51];
int dp[51];
bool preCalc = true;

int main(){
    string input;
    int extrInd = 0;
    int posInd = 0;
    cin >> input;

    //string을 부호가 있는 숫자로 변환 
    for(int i = 0 ; i<input.size();i++){

        if(input[i]=='+'|| input[i]=='-'){
            num[extrInd] = stoi(input.substr(posInd,i));
            posInd = i;
            extrInd++;
        }

    }
    num[extrInd++] = stoi(input.substr(posInd,input.size()));


    for(int i = 1 ; i<= extrInd;i++){

        /*
        다음 마이너스가 나올때까지 양수를 빼준다.
        */
       if(num[i-1]>0){
           //양수이고 앞에 -라면 빼준다. 아니라면 더해준다. 
           if(preCalc == false) dp[i]+=(dp[i-1]-num[i-1]);
           else dp[i]+=(dp[i-1]+num[i-1]);
       }
       else{
           dp[i]+=(dp[i-1]+num[i-1]);
           preCalc= false;
       }
        
            
    }
    cout<<dp[extrInd];
    return 0;
}

