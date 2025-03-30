#include <iostream> 
#include <string>
#include <stack>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
	cin.tie(0);

    string input;
    int Bcount = 0;
    int sum=0;
    char cut;
    stack <char> stick;

    cin >> input;
    for(int ind = 1 ; ind <= input.size(); ind++){
        cut = input.at(ind-1);
        if(cut == '('){
            stick.push('(');
            if(input.at(ind) != ')'){
                Bcount++;
            }
            else{
                stick.pop();
                Bcount--;
            }
        }
        else{
            stick.pop();
            Bcount--;
        }
        sum+=Bcount;
    }

    cout <<sum;

}