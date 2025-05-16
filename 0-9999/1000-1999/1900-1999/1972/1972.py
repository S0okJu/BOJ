import sys 

class SuprisingDetector:
    def __init__(self, inp:str):
        self._str = inp
        self._len = len(self._str)
        
    def _compare_dpair(self, d_num:int) -> bool :
        cmp_set = set()

        for idx in range(0,self._len- d_num - 1):
            splited = self._str[idx] + self._str[idx + d_num + 1]
            if splited in cmp_set:
                return False 

            cmp_set.add(splited)
        return True 

    def work(self) -> str:
        
        if self._len == 1:
            return f"{self._str} is surprising."
        
        for d_num in range(self._len-1):    
            is_success = self._compare_dpair(d_num=d_num)
            
            if not is_success:
                return f"{self._str} is NOT surprising."
                
        return f"{self._str} is surprising."
    
if __name__ == '__main__':
    while True:
        inp = input()
        
        if inp == '*' :
            break
        
        detector = SuprisingDetector(inp=inp)
        print(detector.work())
    