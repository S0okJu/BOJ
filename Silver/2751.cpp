#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
    cin.tie(NULL);
	ios_base::sync_with_stdio(false);
    int N;
    int num;
    vector<int> sorting;
    cin >> N;

    for(int i = 0 ; i < N; i++){
        cin >> num;
        sorting.push_back(num);
    }

    sort(sorting.begin(),sorting.end());


    for(int i = 0 ; i < N; i++){
        cout << sorting[i]<<'\n';
    }

    return 0;
}