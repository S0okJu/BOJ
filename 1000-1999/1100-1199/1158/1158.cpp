#include <iostream>
#include <vector>
using namespace std;

int main(){
    int N, K;
    int index = 0;
    vector<int> arr;
    cin >> N >> K;

    for(int i = 0 ; i < N; i++){
        arr.push_back(i+1);
    }

    cout << "<";
    while(true){
        index = (index+K-1)%arr.size();

        if(arr.size()>1){
            cout << arr[index]<< ", ";
        }
        else{
            cout << arr[index] << ">";
            break;
        }
        
        arr.erase(arr.begin()+index);
    }

    return 0;

}