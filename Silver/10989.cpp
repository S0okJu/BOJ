#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);  

    vector<int> arr;
    int N;  
    int a;
    cin >> N;  

    for(int i = 0 ; i < N ; i++)
    {
        cin >> a;
        arr.push_back(a);
    }
    sort(arr.begin(),arr.end());    

    for(int i = 0 ; i < N; i++)
    {
        cout << arr[i] << '\n';
    }

    return 0;

}