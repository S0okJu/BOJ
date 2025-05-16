import sys
input = sys.stdin.readline

class CustomQueue:
    def __init__(self):
        self._queue = []
    
    def size(self):
        return len(self._queue)
        
    def print_size(self):
        print(self.size())
    
    def print_is_empty(self):
        if self.size() == 0:
            print(1)
        else:
            print(0)
 
    def push(self,x):
        self._queue.append(x)
    
    def pop(self):
        if self.size() == 0:
            print(-1)
        else:
            v = self._queue.pop(0)
            print(v)
    
    def print_front(self):
        if self.size() == 0:
            print(-1)
        else:
            print(self._queue[0])
    
    def print_back(self):
        if self.size() == 0:
            print(-1)
        else:
            print(self._queue[-1])

if __name__ == '__main__':
    queue = CustomQueue()
    N = int(input())

    for i in range(N):
        cmd = list(input().split())
        
        if len(cmd) == 2:
            queue.push(int(cmd[1]))
        else:
            if cmd[0] == "pop":
                queue.pop()
            elif cmd[0] == "size":
                queue.print_size()
            elif cmd[0] == "empty":
                queue.print_is_empty()
            elif cmd[0] == "front":
                queue.print_front()
            elif cmd[0] == "back":
                queue.print_back()