#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

array <int, 100001> v = { 0, };

void binary(int start, int end, int target)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	while (start<=end)
	{
		int middle = (start + end) / 2;

		if (start == end && v[middle] != target)
		{
			cout << "0\n";
            return;
		}

		else if (v[middle] == target)
		{
			cout << "1\n";
			return;
		}

		else if (v[middle] > target)
		{
			end = middle - 1;
			continue;
		}

		else
		{
			start = middle + 1;
			continue;
		}
	}
    cout << "0\n";
}
int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);

	int N, M;

	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> v[i];
	}

	cin >> M;

	sort(v.begin(), v.begin() + N);

	for (int i = 0; i < M; i++)
	{
		int num;

		cin >> num;

		binary(0, N - 1, num);
	}
}