import sys 
input = sys.stdin.readline

class Cookie:
    def __init__(self):
        self._current_flour = 1
        self._current_choco = 1
        self._current_egg = 1
        self._current_butter = 1
        
        self._cond_flour = 1
        self._cond_choco = 1
        self._cond_egg = 1 
        self._cond_butter = 1
        
        self._cookie_cnt = 0
        
    def set_current(self, curr):
        self._current_flour = curr[0]
        self._current_choco = curr[1] 
        self._current_egg = curr[2] 
        self._current_butter = curr[3]
    
    def set_condition(self, cond):
        self._cond_flour = cond[0]
        self._cond_choco = cond[1] 
        self._cond_egg = cond[2] 
        self._cond_butter = cond[3]
    
    def add_flour(self,i):
        self._current_flour += i
        if i > 0:
            print(self._current_flour)
    
        
    def add_choco(self,i):
        self._current_choco += i
        if i > 0:
            print(self._current_choco)
            
        
    def add_butter(self,i):
        self._current_butter += i
        if i > 0:
            print(self._current_butter)
                 
    def add_egg(self,i):
        self._current_egg += i
        if i > 0:
            print(self._current_egg)
    
    def bake(self, i):
        made = []
        
        made.append(int(self._current_flour / self._cond_flour))
        made.append(int(self._current_choco / self._cond_choco))
        made.append(int(self._current_egg / self._cond_egg))
        made.append(int(self._current_butter / self._cond_butter))
        
        cnt = min(made)
        if cnt >= i:
            self._cookie_cnt += i
            print(self._cookie_cnt)
            
            self.add_flour(-(self._cond_flour * i))
            self.add_choco(-(self._cond_choco * i))
            self.add_egg(-(self._cond_egg * i))
            self.add_butter(-(self._cond_butter * i))
        else:
            print('Hello, siumii')


if __name__ == '__main__':
    curr = list(map(int, input().split()))
    cond = list(map(int, input().split()))
    
    cookie = Cookie()
    cookie.set_current(curr)
    cookie.set_condition(cond)
    
    N = int(input())
    for i in range(N):
        cmd, v  = list(map(int, input().split()))
        
        if cmd == 1:
            cookie.bake(v)
        elif cmd == 2:
            cookie.add_flour(v)
        elif cmd == 3:
            cookie.add_choco(v)
        elif cmd == 4:
            cookie.add_egg(v)
        elif cmd == 5:
            cookie.add_butter(v)

    