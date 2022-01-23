#include<iostream>
#include<queue>
#include<vector>
using namespace std;

const long long int MAX = 9876543210;

int main(){
    int N;
    cin >> N;

    vector<long long int> desc; // 줄어드는 숫자가 저장될 vector
    queue<long long int> q;

    for(int i = 0 ; i <10;i++){
        q.push(i);
        desc.push_back(i);
    }
    int idx = 0;
    while(!q.empty()){
        long long int frontValue = q.front();
        cout <<idx++<<": "<< frontValue<<'\n';
        q.pop();

        for(int i = 0; i<frontValue%10;i++){
            long long int n = 10*frontValue+i;
            desc.push_back(n);
            q.push(n);
            cout<<idx++<<": "<<n<<'\n';
        }
    }

    cout << ((N > desc.size())?-1:desc[N-1])<<'\n';
    return 0;

}
