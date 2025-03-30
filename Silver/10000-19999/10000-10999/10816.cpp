#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, M;
    int a;
    int count;
 
    vector<int> Narr;
    vector<int> Marr;
    int *result;

    cin >> N;
    for(int n = 0 ; n < N;n++){
        cin >> a;
        Narr.push_back(a);
    }
    sort(Narr.begin(),Narr.end());

    cin >> M;
    
    for(int m = 0 ; m < M;m++){
        cin >> a;
        Marr.push_back(a);
    }
    result = new int[M];


    for(int i = 0 ; i < M; i++){

        count = 0;
        count = upper_bound(Narr.begin(),Narr.end(),Marr[i]) - lower_bound(Narr.begin(),Narr.end(),Marr[i]);
        result[i] = count;
    }

    for(int i = 0 ; i < M; i++){
        cout << result[i]<<" ";
    }
    delete[] result;

    return 0;
}