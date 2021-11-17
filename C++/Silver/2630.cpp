#include<iostream>
using namespace std;

int matrix[129][129];
int blue, white;
bool func(int a, int b, int size){
    int color = matrix[a][b];
    for(int i = a; i < a+size;i++){
        for(int j = b ; j< b+size;j++){
            if(color!=matrix[i][j])
                return 0;

        }
    }
    return 1;

}
void cut(int a, int b, int n){
    if(!func(a,b,n)){
        cut(a+n/2, b+n/2, n/2);
        cut(a, b+n/2, n/2);
        cut(a+n/2, b, n/2);
        cut(a, b, n/2);
    }
    else{
        if(matrix[a][b]==0){
            white++;
        }
        else{
            blue++;
        }
    }
    return ;
}

int main(){
    int K;
    cin >> K;

    for(int i = 0 ; i < K;i++){
        for(int j = 0 ; j < K;j++){
            cin >> matrix[i][j];
        }
    }
    cut(0,0,K);
    cout << white << '\n'<< blue;
    
}

