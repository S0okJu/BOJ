from sys import stdin
from collections import defaultdict

class LampsMap:
    def __init__(self):
        # 고유 x, y 좌표 저장 (정렬된 리스트로도 활용 가능)
        self.x_set = set()
        self.y_set = set()
        # (x, y) 좌표쌍을 빠르게 찾기 위한 해시셋
        self.point_set = set()
    
    def add_lamp(self, x, y):
        self.x_set.add(x)
        self.y_set.add(y)
        self.point_set.add((x, y))
    
    def is_balanced(self):
        # 1. x, y 고유값 개수로 카테시안 곱이 맞는지 빠르게 체크
        if len(self.x_set) * len(self.y_set) != len(self.point_set):
            return False
        
        # 2. 정렬(문제 분류에 맞춰) 후 모든 조합 존재 확인
        sorted_x = sorted(self.x_set)
        sorted_y = sorted(self.y_set)
        for x in sorted_x:
            for y in sorted_y:
                if (x, y) not in self.point_set:
                    return False
        return True

def main():
    import sys
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        lamps_map = LampsMap()
        for _ in range(N):
            x, y = map(int, input().split())
            lamps_map.add_lamp(x, y)
        print("BALANCED" if lamps_map.is_balanced() else "NOT BALANCED")

if __name__ == "__main__":
    main()
