#include<iostream>
#include<algorithm>
#include<queue>
#include<map>
#include<string>
using namespace std;

string s, ans;
map<string,int> M;
queue<pair<string,int>> q;

int main(){
    int N, K;
    cin >> N >> K;

    for (int i = 0 ; i < N; i++){
        char c;
        cin >> c;
        s.push_back(c);
        // 1 ~ N 까지의 정수를 문자열로 저장하기 위해 '1'을 더한다. 
        // 오름차순이 될때까지 계산하는 문제이므로 문제의 배열을 미리 설정한다. 
        ans.push_back('1'+ i); 
        
    }
    q.push({s, 0});
    M[s];

    while(!q.empty()){
        auto [cur, cost] = q.front();
        q.pop();

        if( cur == ans){
            cout << cost << '\n';
            return 0;
        }

        for(int i = 0 ; i < N - K + 1;i++){
            string temp = cur;
            reverse(temp.begin()+i, temp.begin()+i+K);
            // 맵에서 item 존재 여부를 확인한다. (방문여부 확인)

            if(M.find(temp)==M.end()){ // temp의 값이 존재하지 않는다면 
                q.push({temp, cost+1});
                M[temp]; // 방문 OK

            }
        }
    }
    cout << -1<<'\n';
    return 0;
}