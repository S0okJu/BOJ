#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int sum = 0;
vector<int>input;
vector<int>sorted;
vector<int>map;


void selection_sort(int n,int k){

    for(int i = n-1 ; i >=0;i--){
        if(sorted[i]!=i){
            sorted[map[i]] = sorted[i];
            swap(sorted[i],i);
            k--;

            if(k==0){
                cout << i <<" "<<sorted[i];
            }
            break;
        }
    }
    if(k>0){
        cout<<-1;
    }
}

/*
1.  숫자가 제자리에 없다면, 

*/

int main(){
    int N, K;
    vector<int>input;
    vector<int>sorted;
    vector<int>map;

    cin >> N >> K;

    for(int i = 0 ; i <N;i++){
        int a;
        cin >> a;
        input.push_back(a);
    }

    sorted = input;
    sort(sorted.begin(),sorted.end());
    selection_sort(N,K);

    return 0;

}