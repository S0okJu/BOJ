from collections import deque
import sys

input = sys.stdin.readline

class CustomDeque:
    def __init__(self):
        self._deque = deque()
    
    def push_front(self, x):
        self._deque.appendleft(x)
    
    def push_back(self, x):
        self._deque.append(x)
    
    def pop_front(self):
        if self._size() == 0:
            print(-1)
        else:
            print(self._deque.popleft())
    
    def pop_back(self):
        if self._size() == 0:
            print(-1)
        else:
            print(self._deque.pop())
    
    def _size(self):
        return len(self._deque)
        
    def print_size(self):
        print(self._size())
    
    def print_is_empty(self):
        print(1 if self._size() == 0 else 0)
    
    def print_front(self):
        if self._size() == 0:
            print(-1)
        else:
            print(self._deque[0])
    
    def print_back(self):
        if self._size() == 0:
            print(-1)
        else:
            print(self._deque[-1])
 

if __name__ == '__main__':
    my_deque = CustomDeque()
    N = int(input())

    for _ in range(N):
        cmd = input().split()
        
        if cmd[0] == "push_front":
            my_deque.push_front(int(cmd[1]))
        elif cmd[0] == "push_back":
            my_deque.push_back(int(cmd[1]))
        elif cmd[0] == "pop_front":
            my_deque.pop_front()
        elif cmd[0] == "pop_back":
            my_deque.pop_back()
        elif cmd[0] == "size":
            my_deque.print_size()   
        elif cmd[0] == "empty":
            my_deque.print_is_empty()
        elif cmd[0] == "front":
            my_deque.print_front()
        elif cmd[0] == "back":
            my_deque.print_back()
