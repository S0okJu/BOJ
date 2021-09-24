#include <iostream>

using namespace std;

int k, number;
int order[1024];        // 입력값 순서 배열
int answer[1024];       // 1을 루트노드로 한 노드 순서 배열
int Bcount = 0;

void Seek(int idx, int depth)
{
    if(depth == k)                      // 마지막 층이라면
    {
        answer[idx] = order[Bcount++];   // 해당 노드만 값 넣어주고 끝
    }
    else
    {                                   // 마지막 층이 아니라면
        Seek(idx * 2, depth + 1);       // 왼쪽 자식노드 검사
        answer[idx] = order[Bcount++];   // 현재 노드값 검사, Bcount 증가값에 따라 순서대로 들어가기 때문에 순서가 중요
        Seek(idx * 2 + 1, depth + 1);   // 오른쪽 자식노드 검사
    }
}

int main()
{
    cin >> k;
    number = (1 << k) - 1;
    for(int i = 0 ; i < number ; i++) cin >> order[i];

    Seek(1, 1);

    for(int n = 0, idx = 1 ; n < k ; n++)   // 층별로 출력하기
    {
        for(int i = 0 ; i < 1 << n ; i++)
        {
            
            cout << answer[idx++] << ' ';
        }
        cout << '\n';
    }
}