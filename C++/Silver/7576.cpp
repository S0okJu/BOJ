#include<cstdio>
#include<queue>
using namespace std;

struct T{
    int x, y;
};

int M, N, ans;
int a[1001][1001];
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};// 왼쪽, 오른쪽, 위, 아래를 표현하기 위해
queue<T> box;

void bfs(){
    while(!box.empty()){
        int x = box.front().x;
        int y = box.front().y;
        box.pop();

        for(int i = 0 ; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            // 값이 범위 안에 있거나 0이 아닌 경우 
            if(nx<0 || nx >=N || ny <0||ny>=M) continue;
            if(a[nx][ny]) continue;

            // 0인경우 1(익었음)으로 표시한다. 
            a[nx][ny] = a[x][y]+1;
            box.push({nx,ny});
        }
    }
}


int main() {
    scanf("%d %d", &M, &N);

    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            scanf("%d", &a[i][j]);
            if (a[i][j] == 1) {
                box.push({i, j});
            }
        }
    }
    bfs();
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            if (a[i][j] == 0) {
                printf("-1\n");
                return 0;
            }
            if (ans < a[i][j]) ans = a[i][j];
        }
    }

    printf("\n");

    for(int i = 0 ; i < N;i++){
        for(int j = 0 ; j <M;j++){
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
    printf("%d\n", ans-1);
    return 0;
}


