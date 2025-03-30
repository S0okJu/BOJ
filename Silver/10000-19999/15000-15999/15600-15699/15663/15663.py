import sys
input = sys.stdin.readline

def solution():
    n,m = map(int,input().split()) 
    checked = [False] * n # 각 노드마다 선택되었는지 확인하는 배열
    arr = list(map(int,input().split()))
    arr.sort()
    answer = [-1] * 10 
    
    def backtracking(k):
        if (k==m):
            for i in range(m):
                print(answer[i], end=' ')
            print()
            return

        temp = 0
        # 노드를 모두 순회 
        for i in range(n):
            # 선택이 되지 않거나 이전에 선택한 값과 중복일 경우 
            if not checked[i] and temp != arr[i]:
                answer[k] = arr[i]
                checked[i] = True
                # 현재 숫자로 업데이트
                # sorting을 했기 때문에 이전의 숫자와의 중복 여부만 확인하면 된다. 
                temp = arr[i]
                
                # k==m이 될때까지 노드 탐색 
                backtracking(k+1)
                
                # 백트래킹 
                checked[i]=False

    
    backtracking(0)


if __name__ == '__main__':
    solution()