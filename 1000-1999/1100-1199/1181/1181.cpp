#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

bool cmpWord(string a, string b){
    int aSize = a.size();
    int bSize = b.size();

    if(aSize != bSize){
        return aSize < bSize; // 사이즈대로 정렬 
    }
    else{
        return a < b; // 사이즈가 같을시 사전순 정렬 
    }
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    vector<string> arrWord;

    cin >> N;

    for(int i = 0 ; i < N; i++){
        string a;
        cin >> a;
        arrWord.push_back(a);
    }

    sort(arrWord.begin(),arrWord.end(),cmpWord);
    arrWord.erase(unique(arrWord.begin(),arrWord.end()),arrWord.end());
    
    for(int i = 0 ; i < arrWord.size() ; i++){
        cout << arrWord[i]<<'\n';
    }

    return 0;

    
}