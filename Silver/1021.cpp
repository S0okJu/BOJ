#include <iostream>
#include <deque>
#include <algorithm>
using namespace std;

int N, M;
deque<int> dq;
int main(void)
{

    cin >> N >> M;
    for (int i = 1; i <= N; i++)
        dq.push_back(i);

    int result = 0;

    for (int i = 0; i < M; i++)
    {
        int idx;
        cin >> idx;
        int cur = 1;
        //뽑아내고자 하는 수의 위치
        for (deque<int>::iterator iter = dq.begin(); iter < dq.end(); iter++)
        {
            if (*iter == idx)
                break;
            cur++;
        }

        //왼쪽으로 몇 번 이동했는지.
        int left = cur - 1;

        //오른쪽으로 몇 번 이동했는지.
        int right = dq.size() - cur + 1;

        if (left < right)
        {
            for (int j = 1; j <= left; j++)
            {

                int num = dq.front();
                dq.pop_front();
                dq.push_back(num);
                result++;
            }
            dq.pop_front();
        }

        else

        {

            for (int j = 1; j <= right; j++)
            {

                int num = dq.back();
                dq.pop_back();
                dq.push_front(num);
                result++;
            }
            dq.pop_front();
        }
    }

    cout << result << endl;
    return 0;
}
