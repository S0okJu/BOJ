#include<iostream>
#include<string>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int M;
    int bits = 0;
    string sentence;
    cin >> M;
    for(int i = 0 ; i < M;i++){
        int num;
        cin >> sentence;
        if(sentence=="add"){
            
            cin >> num;
            //or 연산자를 사용해서 num번째 자리수를 1로 채운다.
            bits |=(1<<num);
        }
        else if(sentence=="remove"){
            cin >> num;
            bits &=~(1<<num);
        }
        else if(sentence=="check"){
            cin >> num;

            if(bits&(1<<num)){
                cout<< 1 << '\n';
            }
            else{
                cout<<0<<'\n';
            }
        }
        else if (sentence == "toggle")
        {
            cin >> num;
            bits ^= (1 << num);
        }
        else if (sentence == "all"){
            bits = (1 << 21) - 1;
        }
        else if (sentence == "empty")
        {
            bits = 0;
        }

    }
}