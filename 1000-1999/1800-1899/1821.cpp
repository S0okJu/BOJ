#include<iostream>
using namespace std;

int n,m;
int per[10];
int visit[10];
int arr[10][10];
int idx;
bool solve()
{
	for (int i = 0; i < n; i++)arr[0][i] = per[i];
	for (int i = 1; i < n; i++) {
		for (int j = 0; j < n-i; j++){
		    arr[i][j] = arr[i - 1][j] + arr[i - 1][j + 1];
        }
	}
	if (arr[n - 1][0] == m)return true;
	return false;
}

void permutation(int depth){
    if(depth == n){
        if(solve()){
            for(int i = 0 ; i < n;i++){
                cout<<per[i]<<' ';
            }
            exit(0);
        }
        return;
        
    }

	for (int i = 0; i < n; i++) {
		if (!visit[i]) {
			visit[i] = 1;
			per[depth] = i + 1;
            
			permutation(depth + 1);
			per[depth] = 0;
			visit[i] = 0;
 
		}
	}

}
int main(){
    cin >> n >> m;
    permutation(0);
    return 0;
}
