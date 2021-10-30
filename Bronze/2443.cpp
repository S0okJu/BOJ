#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int start = 1;
    int end = n + (n-1);
    
    int left = start;
    int right = end;
    
    int i,j;
    for(i=1;i<=n;i++){
        for(j=start; j<=right; j++){
            if(j>=left && j <= right){
                cout << "*";
            }
            else{
                cout << " ";
            }
        }
        cout << "\n";
        left++;
        right--;
    }
}