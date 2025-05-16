#include<iostream>
#include<vector>
using namespace std;

int main(){
    int N, M;
    cin >> N >> M;

    // 띄어쓰기 없이 입력받아야 하므로 char을 사용한다.
    vector<vector<char>>matrix(N,vector<char>(M));
    vector<vector<char>>resultMatrix(N,vector<char>(M));
    int res = 0;

    for(int i = 0 ; i < N; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> matrix[i][j];
        }
    }

    for(int i = 0 ; i < N; i++){
        for(int j = 0 ; j < M ; j++){
            cin >> resultMatrix[i][j];
        }
    }

    for(int i = 0 ; i <= N-3;i++){
        for(int j = 0 ; j <= M-3;j++){

            if(matrix[i][j]!=resultMatrix[i][j]){
                res++;
                for(int changeI = i; changeI<i+3;changeI++){
                    for(int changeJ = j ; changeJ<j+3; changeJ++){
                        if(matrix[changeI][changeJ]=='0'){
                            matrix[changeI][changeJ] = '1';
                        }
                        else{
                            matrix[changeI][changeJ] = '0';
                        }
                    }
                }
                
            }

        }
    }
    for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (matrix[i][j] != resultMatrix[i][j])
			{
				cout << "-1";
				return 0;
			}
		}
	}

    cout << res;
    return 0;

}