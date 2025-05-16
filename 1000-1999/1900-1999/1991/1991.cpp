#include<cstdio>
#include<vector>
#include<utility>
using namespace std;

vector<pair<int,int>> T(27);

void preorder(int root){
    int left = T[root].first;
    int right = T[root].second;
    printf("%c", root +'A');
    if(left > 0)
		preorder(left);
	if(right > 0)
		preorder(right);
}
void inorder(int root){
	int left = T[root].first;
	int right = T[root].second;
	if(left > 0)
		inorder(left);
	printf("%c",root+'A');
	if(right > 0)
		inorder(right);
}

void postorder(int root){
	int left = T[root].first;
	int right = T[root].second;
	if(left > 0)
		postorder(left);
	if(right > 0)
		postorder(right);
	printf("%c",root+'A');
}

int main(){
	int N;
	scanf("%d%*c",&N);
	for(int i=0; i<N; i++){
		char root,left,right;
		scanf("%c%*c%c%*c%c%*c",&root,&left,&right);
		T[root-'A'] = make_pair(left-'A',right-'A');
	}	
	
	preorder(0);
	printf("\n");
	
	inorder(0);
	printf("\n");

	postorder(0);
	printf("\n");
}