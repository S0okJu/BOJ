#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int S, J;
vector<int> sang;
vector<int> jung;


int BinarySearch( int len, int target){
    int start = 0;
    int end = len - 1;

    while(start <=end){
        int mid = (start+end)/2;
        if(sang[mid]==target){
            return 1;
        }
        else if(sang[mid]< target){
            start = mid+1;
        }
        else{
            end = mid-1;
        }
    }
    return 0;
}

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> S;
    for(int i = 0 ;  i < S ;i++){
        int a;
        cin >> a;
        sang.push_back(a);
    }
    sort(sang.begin(),sang.end());

    cin >> J;
    for(int j = 0 ; j < J;j++){
        int a;
        cin >> a;
        jung.push_back(a);
    }

    for(int i = 0; i < J;i++){
        int ans = BinarySearch(S,jung[i]);
        cout << ans<<" ";
    }
    return 0;

}