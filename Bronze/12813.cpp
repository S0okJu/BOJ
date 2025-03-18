#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
using namespace std;
const int bit =  100000;
 
int main()
{
    vector<int> AND(bit);
    vector<int> OR(bit);
    vector<int> NOT_A(bit);
    vector<int> NOT_B(bit);
    
    char A[bit],B[bit];
    scanf("%s %s",A,B);
    for(int i=0;i<100000;i++){
        int Now_A=A[i]-'0';// 정수형으로 바꾸기 위해 0을 빼준다. 
        int Now_B=B[i]-'0';
        AND[i]=Now_A && Now_B; // AND
        OR[i]=Now_A || Now_B; // OR
        NOT_A[i]= !Now_A; // Not
        NOT_B[i]= !Now_B; 
    }
    for(int i=0;i<bit;i++){
        printf("%d",AND[i]);
    }
    printf("\n");
    for(int i=0;i<bit;i++){
        printf("%d",OR[i]);
    }
    printf("\n");
    for(int i=0;i<bit;i++){
        printf("%d",OR[i]- AND[i]); //XOR
    }
    printf("\n");
    for(int i=0;i<bit;i++){
        printf("%d",NOT_A[i]);
    }
    printf("\n");
    for(int i=0;i<bit;i++){
        printf("%d",NOT_B[i]);
    }
    printf("\n");
    
}