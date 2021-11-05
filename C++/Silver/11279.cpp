#include <iostream>
using namespace std;

int n,heap[100002],tail=1;

void swap(int &a, int &b) {
	int tmp = a;
	a = b;
	b = tmp;
}
void push(int num) {
	heap[tail] = num;
	int p = tail / 2;
	int cur = tail;
	while (p > 0) {
		if (heap[p] < heap[cur]) {
			swap(heap[p], heap[cur]);
			p /= 2;
			cur /= 2;
		}
		else break;
	}
	tail++;
}
void pop() {
	if (tail == 1) {
		cout << "0\n";
		return;
	}
	cout << heap[1] << '\n';
	heap[1] = heap[--tail];
	int p = 1;

	while (1) {
		int left = p * 2;
		int right = p * 2 + 1;
		if (right<=tail) {
			if (heap[left] < heap[right]) {
				if (heap[right] > heap[p]) {
					swap(heap[right] , heap[p]);
					p = p * 2+1;
				}
				else break;
			}
			else {
				if (heap[left] > heap[p]) {
					swap(heap[left], heap[p]);
					p = p * 2;
				}
				else break;
			}
		}
		else if (left <= tail) {
			if (heap[left] > heap[p]) {
				swap(heap[left], heap[p]);
				p = p * 2;
			}
			else break;
		}
		else break;
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	cin >> n;
	while (n--) {
		int x;
		cin >> x;
		if (x==0) {
			pop();
		}
		else push(x);
	}

	return 0;
}