import sys
input = sys.stdin.readline

class CustomStack:
    def __init__(self):
        self._stack = []
    
    def size(self):
        return len(self._stack)
        
    def print_size(self):
        print(self.size())
    
    def print_is_empty(self):
        if self.size() == 0:
            print(1)
        else:
            print(0)
 
    def push(self,x):
        self._stack.append(x)
    
    def pop(self):
        if self.size() == 0:
            print(-1)
        else:
            v = self._stack.pop()
            print(v)
    
    def print_top(self):
        if self.size() == 0:
            print(-1)
        else:
            print(self._stack[-1])
        

if __name__ == '__main__':
    stack = CustomStack()
    N = int(input())

    for i in range(N):
        cmd = list(input().split())
        
        if len(cmd) == 2:
            stack.push(int(cmd[1]))
        else:
            if cmd[0] == "pop":
                stack.pop()
            elif cmd[0] == "size":
                stack.print_size()
            elif cmd[0] == "empty":
                stack.print_is_empty()
            elif cmd[0] == "top":
                stack.print_top()