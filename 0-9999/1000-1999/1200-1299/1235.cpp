#include<iostream>
#include<string>

using namespace std;

int main(){
    int N;
    int k= 1;
    int checkCount = 0;
    string* student;

    cin >> N; // 학생 수 
    student = new string[N];


    for(int i = 0 ; i < N; i++){
        cin >> student[i];
    }
    
    int numStr = student[0].length();

    while(true){
        checkCount = 0;
        string KstdentNumber[N];

        for(int st = 0 ; st < N; st++){
            KstdentNumber[st] = student[st].substr(numStr-k);
        }// k의 크기만큼 번호를 잘라 새로운 변수에 저장 

        for(int cmpst = 0;  cmpst < N-1; cmpst++){
            for(int i = cmpst+1 ; i <N;i++){
                if(KstdentNumber[i]==KstdentNumber[cmpst]){
                    checkCount = 0;
                    break;
                }// 하나씩 비교하면서 중복 번호가 존재한다면
                else{
                    checkCount=1;
                }

            }
            if(checkCount == 0){ // 중복 번호가 존재한다면 
                k++;
                break;
            }

        }

        if(checkCount !=0){ // 중복 번호가 존재하지 않는다면
            cout << k;
            break;
        }
  
    }
        



    delete[] student;
    return 0;


}