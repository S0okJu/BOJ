#include<iostream>
#include<algorithm>
using namespace std;

int sum = 0;

void selection_sort(int n, int a[],int k){
    for(int last = n-1;last >0;last--){
        int maxN = a[last];
        int loc = last;
        for(int j = 0 ; j <last;j++){
            if(maxN < a[j]){
                maxN = a[j];
                loc = j;
             }
        }
        if(last!=loc){
            swap(a[last],a[loc]);
            sum++;
            if(sum==k){
                for(int i= 0 ; i < n;i++){
                    cout << a[i]<<" ";
                }
                return;
            }
        }

    }
    if(sum < k){
        cout <<-1;
    }
}

int main(){
    int N, K;
    int *input;
    
    cin >> N >> K;

    input = new int[N];
    for(int i = 0 ; i <N;i++){
        cin >> input[i];
    }
    selection_sort(N,input, K);
    delete[] input;
    return 0;

}