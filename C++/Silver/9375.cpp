#include <iostream>
#include <string>
#include <cstring>
#include <map>
using namespace std;
int main(){
    int n, clothNum;
    cin >> n;
    while(n--){
        cin >> clothNum;
        map <string,int> clothes;
        string name, type;
        for(int i = 0; i < clothNum; i++){
            cin >> name >> type;
            clothes[type]++;
        }
        int answer = 1;
        for(auto p = clothes.begin(); p!=clothes.end(); p++)
            answer *= p->second + 1; // 의상의 종류 + 의상을 입지 않는 경우의 수 
        cout << answer - 1 <<'\n'; // 모두 안입는 경우 
    }
}